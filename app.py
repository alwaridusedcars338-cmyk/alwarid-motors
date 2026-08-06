from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# قاعدة بيانات مؤقتة وبسيطة لحفظ السيارات في الذاكرة
# تحتوي على سيارة كمثال افتراضي
CARS_DATABASE = [
    {
        "id": 1,
        "title": "مرسيدس بنز C-Class",
        "price": "145,000 درهم",
        "image": "https://unsplash.com",
        "specs": ["الممشى: 45,000 كم", "الموديل: 2022", "المحرك: 4 سلندر تيربو", "الحالة: ممتازة"]
    }
]

# 1. الصفحة الرئيسية التي يراها الزبائن على جوجل لمشاهدة السيارات
@app.route('/')
def home():
    return render_template('index.html', cars=CARS_DATABASE)

# 2. لوحة التحكم السرية الخاصة بك لإضافة السيارات (رابطها سيكون /admin)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # استقبال البيانات التي ستكتبها بيدك في الاستمارة
        title = request.form.get('title')
        price = request.form.get('price')
        image_url = request.form.get('image_url')
        spec1 = request.form.get('spec1')
        spec2 = request.form.get('spec2')
        spec3 = request.form.get('spec3')
        
        # ترتيب المواصفات في قائمة
        specs_list = [spec1, spec2, spec3]
        specs_list = [s for s in specs_list if s] # تنظيف الخانات الفارغة
        
        # إضافة السيارة الجديدة إلى قاعدة بيانات الموقع فوراً
        new_car = {
            "id": len(CARS_DATABASE) + 1,
            "title": title,
            "price": price,
            "image": image_url if image_url else "https://unsplash.com",
            "specs": specs_list
        }
        CARS_DATABASE.append(new_car)
        return redirect(url_for('home')) # بعد الإضافة يعيدك للصفحة الرئيسية لتشاهد سيارتك الجديدة
        
    return render_template('admin.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
