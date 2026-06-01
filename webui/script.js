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
            if (data.thap_nhi_cung) {
                renderPalaces(data);
            } else if (data.luu_nien) {
                renderAnnualFlow(data);
            }
            renderPatterns(data);
            renderAnalysisContent(data, analysisType);
            jsonOutput.textContent = JSON.stringify(data, null, 2);

            loader.classList.add('hidden');
            resultCard.classList.remove('hidden');
            resultCard.classList.add('animate-fade-in');
            document.querySelector('.tab-btn[data-tab="overview"]').click();
            resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (error) {
            console.error('Failed to generate chart:', error);
            alert('Lỗi kết nối tới API hoặc API bị lỗi: ' + error.message);
            loader.classList.add('hidden');
        }
    });

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

    function renderPalaces(data) {
        if (!data || !data.thap_nhi_cung) return;
        palacesContainer.innerHTML = data.thap_nhi_cung.map(cung => {
            const chinh = cung.chinh_tinh && cung.chinh_tinh.length > 0
                ? cung.chinh_tinh.join(', ')
                : 'Vô Chính Diệu';
            const phu = cung.phu_tinh && cung.phu_tinh.length > 0
                ? cung.phu_tinh.join(', ')
                : null;
            const sat = cung.sat_tinh && cung.sat_tinh.length > 0
                ? cung.sat_tinh.join(', ')
                : null;
            return `
                <div class="palace-card">
                    <div class="palace-header">
                        <span class="palace-name">${cung.ten}</span>
                        <span class="palace-earthly">${cung.dia_chi}${cung.can_cung ? ' (' + cung.can_cung + ')' : ''}</span>
                    </div>
                    <div class="palace-main-stars">${chinh}</div>
                    ${phu ? `<div class="palace-section"><span class="palace-section-label">Phụ tinh</span><span class="palace-section-val">${phu}</span></div>` : ''}
                    ${sat ? `<div class="palace-section"><span class="palace-section-label">Sát tinh</span><span class="palace-section-val">${sat}</span></div>` : ''}
                </div>
            `;
        }).join('');
    }

    function renderAnnualFlow(data) {
        if (!data || !data.luu_nien) return;
        palacesContainer.innerHTML = `
            <div class="palace-card" style="grid-column: 1 / -1;">
                <div class="palace-header">
                    <span class="palace-name">Lưu niên</span>
                </div>
                <pre class="code-block" style="margin-top:8px">${JSON.stringify(data.luu_nien, null, 2)}</pre>
            </div>
        `;
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
