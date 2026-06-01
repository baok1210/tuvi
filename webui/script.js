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
        if (val === 'luunien') {
            luunienOptions.classList.remove('hidden');
        } else if (val === 'ai') {
            aiOptions.classList.remove('hidden');
        }
    });

    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            const paneId = 'pane-' + btn.dataset.tab;
            const pane = document.getElementById(paneId);
            if (pane) pane.classList.add('active');
        });
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        loader.classList.remove('hidden');
        resultCard.classList.add('hidden');

        const formData = new FormData(form);
        const analysisType = analysisTypeSelect.value;

        const payload = {
            nam: parseInt(formData.get('year')),
            thang: parseInt(formData.get('month')),
            ngay: parseInt(formData.get('day')),
            gio: parseInt(formData.get('hour')),
            gioi_tinh: formData.get('gender')
        };

        let url = 'http://localhost:8000/api/v1/chart';

        if (analysisType === 'interpret') {
            url = 'http://localhost:8000/api/v1/chart/interpret';
        } else if (analysisType === 'luunien') {
            url = 'http://localhost:8000/api/v1/chart/luu-nien';
            payload.nam_xem = parseInt(document.getElementById('targetYear').value);
        } else if (analysisType === 'ai') {
            url = 'http://localhost:8000/api/v1/ai/interpret';
            payload.model = document.getElementById('aiModel').value;
        }

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const res = await response.json();
            if (!res.success) {
                throw new Error(res.error || 'Unknown error');
            }

            const data = res.data;
            renderBasicInfo(data);
            renderMenhBan(data);
            renderTuHoa(data);
            renderDaiHan(data);
            if (data.thap_nhi_cung) {
                renderTraditionalBoard(data);
            }
            renderPatterns(data);
            renderAnalysisContent(data, analysisType);
            jsonOutput.textContent = JSON.stringify(data, null, 2);

            loader.classList.add('hidden');
            resultCard.classList.remove('hidden');
            resultCard.classList.add('animate-fade-in');
            document.querySelector('.tab-btn[data-tab="chart"]').click();
            resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (error) {
            console.error('Failed to generate chart:', error);
            alert('Lỗi kết nối tới API hoặc API bị lỗi: ' + error.message);
            loader.classList.add('hidden');
        }
    });

    const BRANCH_POS = {
        "Tỵ": { r: 0, c: 0 }, "Ngọ": { r: 0, c: 1 }, "Mùi": { r: 0, c: 2 }, "Thân": { r: 0, c: 3 },
        "Thìn": { r: 1, c: 0 }, "Dậu": { r: 1, c: 3 },
        "Mão": { r: 2, c: 0 }, "Tuất": { r: 2, c: 3 },
        "Dần": { r: 3, c: 0 }, "Sửu": { r: 3, c: 1 }, "Tý": { r: 3, c: 2 }, "Hợi": { r: 3, c: 3 },
    };

    const DIA_CHI_LIST = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"];

    function tamHopGroup(diaChi) {
        const idx = DIA_CHI_LIST.indexOf(diaChi);
        if (idx === -1) return [];
        // Thân-Tý-Thìn (8-0-4), Dậu-Sửu-Tỵ (9-1-5), Dần-Ngọ-Tuất (2-6-10), Mão-Mùi-Hợi (3-7-11)
        const groupStarts = [0, 1, 2, 3];
        for (const gs of groupStarts) {
            const group = [gs, (gs + 4) % 12, (gs + 8) % 12];
            if (group.includes(idx)) return group;
        }
        return [];
    }

    function renderTraditionalBoard(data) {
        if (!data || !data.thap_nhi_cung) return;

        const grid = [[], [], [], []];
        data.thap_nhi_cung.forEach(cung => {
            const pos = BRANCH_POS[cung.dia_chi];
            if (!pos) return;
            if (!grid[pos.r][pos.c]) grid[pos.r][pos.c] = [];
            grid[pos.r][pos.c].push(cung);
        });

        const info = data.thong_tin_co_ban || {};
        const menh = data.menh_ban || {};

        // Build 4x4 grid HTML
        let html = '<div class="tv-board">';
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 4; c++) {
                if (r >= 1 && r <= 2 && c >= 1 && c <= 2) {
                    if (r === 1 && c === 1) {
                        html += `<div class="tv-center">
                            <div class="tv-center-title">TỬ VI ĐẨU SỐ</div>
                            <div class="tv-center-info">
                                <div><span class="tv-ci-label">Dương lịch</span><span class="tv-ci-val">${info.duong_lich || ''}</span></div>
                                <div><span class="tv-ci-label">Âm lịch</span><span class="tv-ci-val">${info.am_lich || ''}</span></div>
                                <div><span class="tv-ci-label">Năm</span><span class="tv-ci-val">${info.nam_can_chi || ''}</span></div>
                                <div><span class="tv-ci-label">Mệnh</span><span class="tv-ci-val">${menh.cung_menh || ''}</span></div>
                                <div><span class="tv-ci-label">Thân</span><span class="tv-ci-val">${menh.cung_than || ''}</span></div>
                                <div><span class="tv-ci-label">Cục</span><span class="tv-ci-val">${menh.cuc || ''}</span></div>
                                <div><span class="tv-ci-label">Giới tính</span><span class="tv-ci-val">${info.gioi_tinh || ''}</span></div>
                            </div>
                        </div>`;
                    }
                    continue;
                }
                const cungs = grid[r][c];
                const cung = cungs ? cungs[0] : null;
                if (cung) {
                    const chinh = cung.chinh_tinh && cung.chinh_tinh.length > 0
                        ? cung.chinh_tinh.join('<br>') : 'Vô Chính Diệu';
                    const phu = cung.phu_tinh && cung.phu_tinh.length > 0
                        ? cung.phu_tinh.join(', ') : null;
                    const sat = cung.sat_tinh && cung.sat_tinh.length > 0
                        ? cung.sat_tinh.join(', ') : null;
                    const dt = cung.dac_tinh && Object.keys(cung.dac_tinh).length > 0
                        ? Object.entries(cung.dac_tinh).map(([s, v]) => `${s}(${v})`).join(', ') : null;
                    const thanClass = cung.is_than ? ' tv-cell-than' : '';
                    const diaChiIdx = DIA_CHI_LIST.indexOf(cung.dia_chi);
                    html += `<div class="tv-cell${thanClass}" data-idx="${diaChiIdx}">
                        <div class="tv-cell-header">
                            <span class="tv-cell-name">${cung.ten}</span>
                            <span class="tv-cell-branch">${cung.dia_chi}${cung.can_cung ? '(' + cung.can_cung + ')' : ''}</span>
                            ${cung.is_than ? '<span class="than-badge">Thân</span>' : ''}
                        </div>
                        <div class="tv-cell-stars">${chinh}</div>
                        ${dt ? `<div class="tv-cell-dt">${dt}</div>` : ''}
                        ${phu ? `<div class="tv-cell-phu">${phu}</div>` : ''}
                        ${sat ? `<div class="tv-cell-sat">${sat}</div>` : ''}
                    </div>`;
                } else {
                    html += '<div class="tv-cell tv-cell-empty"></div>';
                }
            }
        }
        html += '</div>';
        palacesContainer.innerHTML = html;

        // Click interaction for Tam Hop + Xung Chieu
        const cells = palacesContainer.querySelectorAll('.tv-cell[data-idx]');
        cells.forEach(cell => {
            cell.addEventListener('click', () => {
                const idx = parseInt(cell.dataset.idx);
                const diaChi = DIA_CHI_LIST[idx];
                const tamHop = tamHopGroup(diaChi);
                const xungChieu = (idx + 6) % 12;
                cells.forEach(c => c.classList.remove('tv-cell-highlight', 'tv-cell-xung'));
                const allIdx = new Set(tamHop);
                allIdx.add(xungChieu);
                cells.forEach(c => {
                    const ci = parseInt(c.dataset.idx);
                    if (allIdx.has(ci)) {
                        const dc = DIA_CHI_LIST[ci];
                        c.classList.add(tamHop.includes(ci) ? 'tv-cell-highlight' : 'tv-cell-xung');
                    }
                });
                // Toggle off if clicking the same cell again
                if (cell.classList.contains('tv-cell-highlight')) {
                    const ci = parseInt(cell.dataset.idx);
                    const sameCellClicked = cell.dataset._last === String(idx);
                    if (sameCellClicked) {
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
        const items = [
            { label: 'Dương Lịch', value: info.duong_lich },
            { label: 'Âm Lịch', value: info.am_lich },
            { label: 'Năm Can Chi', value: info.nam_can_chi },
            { label: 'Giới Tính', value: info.gioi_tinh },
        ];
        basicInfoGrid.innerHTML = items.map(item => `
            <div class="info-item">
                <span class="info-label">${item.label}</span>
                <span class="info-value">${item.value || 'N/A'}</span>
            </div>
        `).join('');
    }

    function renderMenhBan(data) {
        if (!data) return;
        const menh = data.menh_ban || {};
        const items = [
            { label: 'Cung Mệnh', value: menh.cung_menh },
            { label: 'Cung Thân', value: menh.cung_than },
            { label: 'Cục', value: menh.cuc },
            { label: 'Hành', value: menh.hanh },
        ];
        menhBanGrid.innerHTML = items.map(item => `
            <div class="info-item">
                <span class="info-label">${item.label}</span>
                <span class="info-value">${item.value || 'N/A'}</span>
            </div>
        `).join('');
    }

    function renderTuHoa(data) {
        const th = data.tu_hoa;
        if (!th) return;
        const container = document.getElementById('tuHoaGrid');
        if (!container) return;
        const labels = { Lộc: 'Hóa Lộc', Quyền: 'Hóa Quyền', Khoa: 'Hóa Khoa', Kỵ: 'Hóa Kỵ' };
        container.innerHTML = Object.entries(th).map(([k, v]) => `
            <div class="tuhoa-item ${k.toLowerCase()}">
                <span class="tuhoa-label">${labels[k] || k}</span>
                <span class="tuhoa-value">${v || '-'}</span>
            </div>
        `).join('');
    }

    function renderDaiHan(data) {
        if (!data || !data.dai_han || data.dai_han.length === 0) return;
        const container = document.getElementById('daiHanGrid');
        if (!container) return;
        container.innerHTML = data.dai_han.map(dh => `
            <div class="daihan-item">
                <span class="daihan-cung">${dh.cung}</span>
                <span class="daihan-tuoi">${dh.tuoi}</span>
            </div>
        `).join('');
    }

    function renderPatterns(data) {
        const container = document.getElementById('patternsContent');
        if (!container) return;
        const patterns = data.cach_cuc || [];
        const combos = data.ket_hop_sao || [];
        let html = '';
        if (patterns.length > 0) {
            html += '<div class="interpret-section"><div class="interpret-title">Cách cục</div>';
            html += patterns.map(p => `<div class="pattern-item"><strong>${p.cach_cuc || p.ten || '?'}</strong>: ${p.y_nghia || p.mo_ta || ''}</div>`).join('');
            html += '</div>';
        }
        if (combos.length > 0) {
            html += '<div class="interpret-section"><div class="interpret-title">Kết hợp sao</div>';
            html += combos.map(c => `<div class="pattern-item"><strong>${c.ten || '?'}</strong>: ${c.y_nghia || c.mo_ta || ''}</div>`).join('');
            html += '</div>';
        }
        container.innerHTML = html || '';
    }

    function renderAnalysisContent(data, type) {
        analysisContent.innerHTML = '';
        if (type === 'ai' && data.interpretation) {
            analysisContent.innerHTML = `
                <div class="interpret-section">
                    <div class="interpret-title">Luận giải bởi AI (${data.model})</div>
                    <div class="ai-interpretation">${data.interpretation}</div>
                </div>
            `;
        } else if (type === 'interpret' && data.luan_giai) {
            analysisContent.innerHTML = data.luan_giai.map(gd => `
                <div class="interpret-section">
                    <div class="interpret-title">${gd.cung} - ${gd.tieu_de}</div>
                    <div class="interpret-text">
                        ${(gd.phan_tich || []).map(pt => `<p>• ${pt}</p>`).join('')}
                    </div>
                </div>
            `).join('');
        } else {
            const patterns = data.cach_cuc || [];
            if (patterns.length > 0) {
                analysisContent.innerHTML = `
                    <div class="interpret-section">
                        <div class="interpret-title">Cách cục nhận diện</div>
                        <div class="interpret-text">
                            ${patterns.map(p => `<p><strong>${p.cach_cuc || p.ten}:</strong> ${p.y_nghia || ''}</p>`).join('<br>')}
                        </div>
                    </div>
                `;
            } else {
                analysisContent.innerHTML = '<p class="interpret-text">Chọn chế độ "Luận giải chi tiết" để xem phân tích từng cung.</p>';
            }
        }
    }
});
