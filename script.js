document.addEventListener('DOMContentLoaded', () => {
    const fileList = document.getElementById('file-list');
    const dropZone = document.getElementById('drop-zone');

    // وظيفة وهمية (Mock Function) لتمثيل تحميل ملف
    function simulateFileUpload(fileName) {
        alert(`تم محاولة رفع الملف: ${fileName}\n\nملاحظة: هذا مجرد نموذج واجهة أمامي. عملية الرفع الفعلية تتطلب بنية خلفية (Backend) قوية.`);
        
        // يمكن إضافة الملف بشكل وهمي إلى القائمة
        const newItem = document.createElement('li');
        newItem.classList.add('file-item', 'document'); // نفترض أنه مستند
        newItem.innerHTML = `
            <i class="fas fa-file"></i>
            <span class="file-name">${fileName}</span>
            <span>الآن</span>
            <span>حجم وهمي</span>
            <span>خاص</span>
        `;
        fileList.prepend(newItem);
    }

    // تفعيل منطقة السحب والإفلات
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.backgroundColor = '#e0f7ff';
        dropZone.style.borderColor = var('--primary-color');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.backgroundColor = '#fff';
        dropZone.style.borderColor = '#e9ecef';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.style.backgroundColor = '#fff';
        dropZone.style.borderColor = '#e9ecef';

        if (e.dataTransfer.items) {
            for (let i = 0; i < e.dataTransfer.items.length; i++) {
                // نأخذ الملف الأول كنموذج فقط
                const file = e.dataTransfer.items[i].getAsFile();
                if (file) {
                    simulateFileUpload(file.name);
                    break; 
                }
            }
        }
    });

    // إضافة تفاعل عند الضغط على زر الرفع
    const uploadBtn = document.querySelector('.upload-btn');
    uploadBtn.addEventListener('click', () => {
        alert("وظيفة الرفع قيد التطوير (تتطلب Backend).");
    });
});
