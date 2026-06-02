document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chartForm');
    const loader = document.getElementById('loader');
    const resultCard = document.getElementById('result');
    const basicInfoGrid = document.getElementById('basicInfoGrid');
    const menhBanGrid = document.getElementById('menhBanGrid');
    const palacesContainer = document.getElementById('palacesContainer');
    const analysisContent = document.getElementById('analysisContent');
    const jsonOutput = document.getElementById('jsonOutput');
    const analysisTypeSelect = document.getElementById('analysisType');
    const luunienOptions = document.getElementById('luunien-options');
    const aiOptions = document.getElementById('ai-options');

    analysisTypeSelect.addEventListener('change', () => {
        const val = analysisTypeSelect.value;
        luunienOptions.classList.add('hidden');
        aiOptions.classList.add('hidden');
        if (val === 'luunien') luunienOptions.classList.remove('hidden');
        else if (val === 'ai') aiOptions.classList.remove('hidden');
    });

    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            const pane = document.getElementById('pane-' + btn.dataset.tab);
            if (pane) pane.classList.add('active');
        });
    });

    const featureToggles = document.querySelectorAll('.toggle-btn');
    featureToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            toggle.classList.toggle('active');
            const sections = document.querySelectorAll(`.feature-${toggle.dataset.feature}`);
            sections.forEach(s => s.style.display = toggle.classList.contains('active') ? '' : 'none');
        });
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        loader.classList.remove('hidden');
        resultCard.classList.add('hidden');

        const formData = new FormData(form);
        const analysisType = analysisTypeSelect.value;
        const nam = parseInt(formData.get('year'));
        const thang = parseInt(formData.get('month'));
        const ngay = parseInt(formData.get('day'));
        const gio = parseInt(formData.get('hour'));
        const gioiTinh = formData.get('gender');

        try {
            // Client-side an sao
            const chartData = createChart(nam, thang, ngay, gio, gioiTinh);

            if (analysisType === 'interpret') {
                chartData.luan_giai = giaiDoanToanBo(chartData).map(gd => ({
                    cung: gd.ten, tieu_de: gd.tieu_de,
                    phan_tich: gd.sao_phan_tich.map(s => `${s.sao}: ${s.giai_doan}`)
                }));
            }

            if (analysisType === 'luunien') {
                // Simplified flow-year (basic)
                const namXem = parseInt(document.getElementById('targetYear').value);
                chartData.luu_nien = { nam_xem: namXem, ghi_chu: "Luận giải lưu niên cơ bản" };
            }

            // Run patterns, scoring locally
            chartData.cach_cuc = nhanDienCachCuc(chartData);
            chartData.diem_so = tinhDiemToanBo(chartData.thap_nhi_cung, chartData.tu_hoa);

            if (analysisType === 'ai') {
                const apiKey = document.getElementById('apiKey').value;
                const model = document.getElementById('aiModel').value;
                if (!apiKey) throw new Error('Vui lòng nhập API Key để dùng AI');
                await callAI(chartData, apiKey, model, gioiTinh);
            }

            renderBasicInfo(chartData);
            renderMenhBan(chartData);
            renderTuHoa(chartData);
            renderDaiHan(chartData);
            if (chartData.thap_nhi_cung) renderTraditionalBoard(chartData);
            renderPatterns(chartData);
            renderScoring(chartData);
            renderBacPhaiAnalysis(chartData);
            renderAnalysisContent(chartData, analysisType);
            jsonOutput.textContent = JSON.stringify(chartData, null, 2);

            loader.classList.add('hidden');
            resultCard.classList.remove('hidden');
            resultCard.classList.add('animate-fade-in');
            document.querySelector('.tab-btn[data-tab="chart"]').click();
            resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (error) {
            console.error('Lỗi:', error);
            alert('Lỗi: ' + error.message);
            loader.classList.add('hidden');
        }
    });

    async function callAI(chartData, apiKey, model, gioiTinh) {
        const isOpenAI = model.startsWith('gpt');
        const isClaude = model.startsWith('claude');
        const url = isOpenAI ? 'https://api.openai.com/v1/chat/completions'
                   : isClaude ? 'https://api.anthropic.com/v1/messages' : null;
        if (!url) throw new Error('Model không hỗ trợ');

        const chartSummary = {
            thong_tin_co_ban: chartData.thong_tin_co_ban,
            menh_ban: chartData.menh_ban,
            tu_hoa: chartData.tu_hoa,
            thap_nhi_cung: chartData.thap_nhi_cung.map(c => ({
                ten: c.ten, dia_chi: c.dia_chi, chinh_tinh: c.chinh_tinh,
                phu_tinh: c.phu_tinh, sat_tinh: c.sat_tinh, dac_tinh: c.dac_tinh
            })),
            dai_han: chartData.dai_han,
            cach_cuc: chartData.cach_cuc,
        };

        const systemPrompt = `Bạn là chuyên gia Tử Vi Đẩu Số. Phân tích lá số chi tiết dựa trên dữ liệu được cung cấp. Trả lời bằng tiếng Việt, giọng văn chuyên nghiệp. Phân tích từng cung, ý nghĩa các sao, cách cục, tứ hóa, đại hạn. Đưa ra nhận xét tổng quan và lời khuyên.`;

        const userPrompt = `Hãy luận giải lá số tử vi sau:\n${JSON.stringify(chartSummary, null, 2)}\n\nGiới tính: ${gioiTinh}\n\nPhân tích chi tiết từng cung và đưa ra nhận xét tổng quan.`;

        let interpretation;
        if (isOpenAI) {
            const res = await fetch(url, {
                method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${apiKey}` },
                body: JSON.stringify({ model, messages: [{role:'system',content:systemPrompt},{role:'user',content:userPrompt}], temperature:0.7, max_tokens:4096 })
            });
            const data = await res.json();
            if (!res.ok) throw new Error(data.error?.message || 'OpenAI API error');
            interpretation = data.choices[0].message.content;
        } else if (isClaude) {
            const res = await fetch(url, {
                method: 'POST', headers: { 'Content-Type': 'application/json', 'x-api-key': apiKey, 'anthropic-version':'2023-06-01' },
                body: JSON.stringify({ model, max_tokens:4096, system:systemPrompt, messages:[{role:'user',content:userPrompt}] })
            });
            const data = await res.json();
            if (!res.ok) throw new Error(data.error?.message || 'Anthropic API error');
            interpretation = data.content[0].text;
        }

        chartData.interpretation = interpretation;
        chartData.model = model;
    }

    // Board rendering functions (unchanged from original)
    const BRANCH_POS = {
        "Tỵ":{r:0,c:0},"Ngọ":{r:0,c:1},"Mùi":{r:0,c:2},"Thân":{r:0,c:3},
        "Thìn":{r:1,c:0},"Dậu":{r:1,c:3},"Mão":{r:2,c:0},"Tuất":{r:2,c:3},
        "Dần":{r:3,c:0},"Sửu":{r:3,c:1},"Tý":{r:3,c:2},"Hợi":{r:3,c:3},
    };
    const DIA_CHI_LIST = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"];

    function tamHopGroup(diaChi) {
        const idx = DIA_CHI_LIST.indexOf(diaChi);
        if (idx === -1) return [];
        for (const gs of [0,1,2,3]) {
            const group = [gs, (gs+4)%12, (gs+8)%12];
            if (group.includes(idx)) return group;
        }
        return [];
    }

    function renderTraditionalBoard(data) {
        if (!data || !data.thap_nhi_cung) return;
        const tuHoaMap = {};
        const th = data.tu_hoa || {};
        for (const [key, star] of Object.entries(th)) if (star) tuHoaMap[star.toLowerCase()] = key;

        function starWithBadge(name) {
            const ht = tuHoaMap[name.toLowerCase()];
            if (ht) {
                const cls = ht==='Hóa Lộc'?'hb-loc':ht==='Hóa Quyền'?'hb-quyen':ht==='Hóa Khoa'?'hb-khoa':'hb-ky';
                const label = ht==='Hóa Lộc'?'L':ht==='Hóa Quyền'?'Q':ht==='Hóa Khoa'?'K':'Kỵ';
                return `${name}<span class="tv-hoa-badge ${cls}">${label}</span>`;
            }
            return name;
        }

        const grid = [[],[],[],[]];
        data.thap_nhi_cung.forEach(cung => {
            const pos = BRANCH_POS[cung.dia_chi];
            if (!pos) return;
            if (!grid[pos.r][pos.c]) grid[pos.r][pos.c] = [];
            grid[pos.r][pos.c].push(cung);
        });

        const info = data.thong_tin_co_ban || {};
        const menh = data.menh_ban || {};

        let html = '<div class="tv-board">';
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 4; c++) {
                if (r >= 1 && r <= 2 && c >= 1 && c <= 2) {
                    if (r === 1 && c === 1) {
                        html += `<div class="tv-center"><div class="tv-center-title">TỬ VI ĐẨU SỐ</div><div class="tv-center-info">
                            <div><span class="tv-ci-label">Dương lịch</span><span class="tv-ci-val">${info.duong_lich||''}</span></div>
                            <div><span class="tv-ci-label">Âm lịch</span><span class="tv-ci-val">${info.am_lich||''}</span></div>
                            <div><span class="tv-ci-label">Năm</span><span class="tv-ci-val">${info.nam_can_chi||''}</span></div>
                            <div><span class="tv-ci-label">Mệnh</span><span class="tv-ci-val">${menh.cung_menh||''}</span></div>
                            <div><span class="tv-ci-label">Thân</span><span class="tv-ci-val">${menh.cung_than||''}</span></div>
                            <div><span class="tv-ci-label">Cục</span><span class="tv-ci-val">${menh.cuc||''}</span></div>
                            <div><span class="tv-ci-label">Giới tính</span><span class="tv-ci-val">${info.gioi_tinh||''}</span></div>
                        </div></div>`;
                    }
                    continue;
                }
                const cungs = grid[r][c];
                const cung = cungs ? cungs[0] : null;
                if (cung) {
                    const chinh = cung.chinh_tinh?.length ? cung.chinh_tinh.map(starWithBadge).join('<br>') : 'Vô Chính Diệu';
                    const phu = cung.phu_tinh?.length ? cung.phu_tinh.join(', ') : null;
                    const sat = cung.sat_tinh?.length ? cung.sat_tinh.join(', ') : null;
                    const dt = cung.dac_tinh && Object.keys(cung.dac_tinh).length ? Object.entries(cung.dac_tinh).map(([s,v])=>`${s}(${v})`).join(', ') : null;
                    const thanClass = cung.is_than ? ' tv-cell-than' : '';
                    html += `<div class="tv-cell${thanClass}" data-idx="${DIA_CHI_LIST.indexOf(cung.dia_chi)}">
                        <div class="tv-cell-header"><span class="tv-cell-name">${cung.ten}</span><span class="tv-cell-branch">${cung.dia_chi}${cung.can_cung?'('+cung.can_cung+')':''}</span>${cung.is_than?'<span class="than-badge">Thân</span>':''}</div>
                        <div class="tv-cell-stars">${chinh}</div>
                        ${dt?`<div class="tv-cell-dt">${dt}</div>`:''}
                        ${phu?`<div class="tv-cell-phu">${phu}</div>`:''}
                        ${sat?`<div class="tv-cell-sat">${sat}</div>`:''}
                    </div>`;
                } else {
                    html += '<div class="tv-cell tv-cell-empty"></div>';
                }
            }
        }
        html += '</div>';
        palacesContainer.innerHTML = html;

        const cells = palacesContainer.querySelectorAll('.tv-cell[data-idx]');
        cells.forEach(cell => {
            cell.addEventListener('click', () => {
                const idx = parseInt(cell.dataset.idx);
                const tamHop = tamHopGroup(DIA_CHI_LIST[idx]);
                const xungChieu = (idx + 6) % 12;
                cells.forEach(c => c.classList.remove('tv-cell-highlight', 'tv-cell-xung'));
                const allIdx = new Set(tamHop);
                allIdx.add(xungChieu);
                cells.forEach(c => {
                    const ci = parseInt(c.dataset.idx);
                    if (allIdx.has(ci)) c.classList.add(tamHop.includes(ci) ? 'tv-cell-highlight' : 'tv-cell-xung');
                });
                if (cell.classList.contains('tv-cell-highlight')) {
                    if (cell.dataset._last === String(idx)) {
                        cells.forEach(c => c.classList.remove('tv-cell-highlight', 'tv-cell-xung'));
                        cells.forEach(c => delete c.dataset._last);
                        return;
                    }
                    cell.dataset._last = idx;
                }
            });
        });
    }

    function renderBasicInfo(data) {
        if (!data) return;
        const info = data.thong_tin_co_ban || {};
        basicInfoGrid.innerHTML = [
            {label:'Dương Lịch',value:info.duong_lich},{label:'Âm Lịch',value:info.am_lich},
            {label:'Năm Can Chi',value:info.nam_can_chi},{label:'Giới Tính',value:info.gioi_tinh},
        ].map(item => `<div class="info-item"><span class="info-label">${item.label}</span><span class="info-value">${item.value||'N/A'}</span></div>`).join('');
    }

    function renderMenhBan(data) {
        if (!data) return;
        const menh = data.menh_ban || {};
        menhBanGrid.innerHTML = [
            {label:'Cung Mệnh',value:menh.cung_menh},{label:'Cung Thân',value:menh.cung_than},
            {label:'Cục',value:menh.cuc},{label:'Hành',value:menh.hanh},
        ].map(item => `<div class="info-item"><span class="info-label">${item.label}</span><span class="info-value">${item.value||'N/A'}</span></div>`).join('');
    }

    function renderTuHoa(data) {
        const th = data.tu_hoa;
        if (!th) return;
        const container = document.getElementById('tuHoaGrid');
        if (!container) return;
        const labels = {'Hóa Lộc':'Hóa Lộc','Hóa Quyền':'Hóa Quyền','Hóa Khoa':'Hóa Khoa','Hóa Kỵ':'Hóa Kỵ'};
        container.innerHTML = Object.entries(th).map(([k,v]) =>
            `<div class="tuhoa-item ${k==='Hóa Lộc'?'loc':k==='Hóa Quyền'?'quyen':k==='Hóa Khoa'?'khoa':'ky'}">
                <span class="tuhoa-label">${labels[k]||k}</span><span class="tuhoa-value">${v||'-'}</span>
            </div>`
        ).join('');
    }

    function renderDaiHan(data) {
        if (!data || !data.dai_han?.length) return;
        const container = document.getElementById('daiHanGrid');
        if (!container) return;
        container.innerHTML = data.dai_han.map(dh =>
            `<div class="daihan-item"><span class="daihan-cung">${dh.cung}</span><span class="daihan-tuoi">${dh.tuoi}</span></div>`
        ).join('');
    }

    function renderPatterns(data) {
        const container = document.getElementById('patternsContent');
        if (!container) return;
        const patterns = data.cach_cuc || [];
        let html = '';
        if (patterns.length > 0) {
            html += '<div class="interpret-section"><div class="interpret-title">Cách cục</div>';
            html += patterns.map(p => `<div class="pattern-item"><strong>${p.cach_cuc||'?'}</strong>: ${p.y_nghia||''}${p.source?`<span class="source-tag">${p.source}</span>`:''}</div>`).join('');
            html += '</div>';
        }
        container.innerHTML = html || '';
    }

    function renderScoring(data) {
        const container = document.getElementById('scoringContent');
        if (!container) return;
        const diem = data.diem_so;
        if (!diem) return;
        const totalScore = diem.diem_trung_binh || 50;
        const totalClass = totalScore>=70?'score-good':totalScore>=50?'score-avg':totalScore>=30?'score-poor':'score-bad';
        let html = `<div class="score-summary"><div class="score-gauge"><div class="score-ring ${totalClass}"><span>${totalScore}</span></div>
            <div class="score-label">Tổng quan <small>${diem.xep_loai_tong_quan||''}</small></div></div><div class="score-dimensions">`;
        if (diem.cac_khia_canh) {
            for (const [dim, info] of Object.entries(diem.cac_khia_canh)) {
                const cls = info.diem>=70?'score-good':info.diem>=50?'score-avg':info.diem>=30?'score-poor':'score-bad';
                html += `<div class="score-dim"><div class="score-dim-bar"><span class="dim-fill ${cls}" style="width:${info.diem}%"></span></div>
                    <div class="score-dim-label">${dim} <strong>${info.diem}</strong> <small>${info.xep_loai||''}</small></div></div>`;
            }
        }
        html += '</div><div class="score-palaces">';
        if (diem.tung_cung) {
            Object.entries(diem.tung_cung).sort((a,b)=>b[1].diem-a[1].diem).forEach(([ten, info]) => {
                const cls = info.diem>=70?'score-good':info.diem>=50?'score-avg':info.diem>=30?'score-poor':'score-bad';
                html += `<div class="score-palace-item"><span class="spi-name">${ten}</span>
                    <span class="spi-bar"><span class="spi-fill ${cls}" style="width:${info.diem}%"></span></span>
                    <span class="spi-score">${info.diem}</span><span class="spi-rank">${info.xep_loai||''}</span></div>`;
            });
        }
        html += '</div></div>';
        container.innerHTML = html;
    }

    function renderBacPhaiAnalysis(data) {
        const container = document.getElementById('bacphaiContent');
        if (!container) return;
        container.innerHTML = '<p class="interpret-text">Tính năng Bắc Phái yêu cầu backend Python. Chọn chế độ AI để kích hoạt.</p>';
    }

    function renderAnalysisContent(data, type) {
        analysisContent.innerHTML = '';
        if (type === 'ai' && data.interpretation) {
            analysisContent.innerHTML = `<div class="interpret-section"><div class="interpret-title">Luận giải bởi AI (${data.model||''})</div>
                <div class="ai-interpretation">${data.interpretation}</div></div>`;
        } else if (type === 'interpret' && data.luan_giai) {
            analysisContent.innerHTML = data.luan_giai.map(gd =>
                `<div class="interpret-section"><div class="interpret-title">${gd.cung} - ${gd.tieu_de}</div>
                <div class="interpret-text">${(gd.phan_tich||[]).map(pt => `<p>• ${pt}</p>`).join('')}</div></div>`
            ).join('');
        } else if (type === 'luunien') {
            analysisContent.innerHTML = `<div class="interpret-section"><div class="interpret-title">Lưu niên</div>
                <div class="interpret-text"><p>Tính năng lưu niên nâng cao yêu cầu backend Python. Phiên bản cơ bản hiển thị tại đây.</p></div></div>`;
        } else {
            const patterns = data.cach_cuc || [];
            analysisContent.innerHTML = patterns.length > 0
                ? `<div class="interpret-section"><div class="interpret-title">Cách cục nhận diện</div>
                    <div class="interpret-text">${patterns.map(p => `<p><strong>${p.cach_cuc}:</strong> ${p.y_nghia||''}</p>`).join('<br>')}</div></div>`
                : '<p class="interpret-text">Chọn chế độ "Luận giải chi tiết" để xem phân tích từng cung.</p>';
        }
    }
});
