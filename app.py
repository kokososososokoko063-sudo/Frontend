import os
from flask import Flask, request, redirect, url_for, render_template

# تحديد مسار لحفظ الملفات التي تم رفعها (يجب أن يكون آمناً)
UPLOAD_FOLDER = 'uploaded_files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# إنشاء مجلد الحفظ إذا لم يكن موجوداً
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """التحقق من امتداد الملف"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """عرض نموذج الرفع"""
    # لعرض الواجهة الأمامية، يجب أن يكون لديك ملف index.html في مجلد templates
    # (لكن هنا سنستخدم استجابة نصية بسيطة)
    return """
    <!doctype html>
    <title>نموذج رفع ملفات</title>
    <h1 style="direction: rtl;">رفع ملف جديد</h1>
    <form method=post enctype=multipart/form-data style="direction: rtl; text-align: right;">
      <input type=file name=file>
      <input type=submit value=رفع>
    </form>
    """

@app.route('/upload', methods=['POST'])
def upload_file():
    """معالجة طلبات رفع الملفات"""
    # 1. التحقق من وجود الملف في الطلب
    if 'file' not in request.files:
        return 'لم يتم تحديد ملف في الطلب', 400
    
    file = request.files['file']
    
    # 2. التحقق من اسم الملف
    if file.filename == '':
        return 'لم يتم اختيار ملف', 400
    
    # 3. التحقق من نوع الملف وحفظه
    if file and allowed_file(file.filename):
        filename = file.filename
        # هنا يتم حفظ الملف على الخادم المحلي (في بيئة الإنتاج، يتم إرساله إلى S3)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # رسالة نجاح بسيطة
        return f'تم رفع الملف "{filename}" بنجاح! تم حفظه محلياً.', 200
    
    return 'امتداد الملف غير مسموح به', 400

# لربط مسار URL بالجزء الأمامي (index.html)
app.add_url_rule('/files', 'upload_file', upload_file)

if __name__ == '__main__':
    # لتشغيل الخادم، استخدم: python app.py
    app.run(debug=True)
