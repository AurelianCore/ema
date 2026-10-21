import os
import json

# المسار الأساسي لمجلد الموسيقى وملف المخرجات
MUSIC_DIR = "music"
OUTPUT_JSON = "songs.json"

# الامتدادات الصوتية المدعومة
AUDIO_EXTENSIONS = ('.mp3', '.m4a', '.wav', '.ogg', '.flac')

songs_list = []

print("جاري فحص مجلدات الأغاني وتوليد القائمة... 🎵💙")

if os.path.exists(MUSIC_DIR):
    # المرور على المجلدات الفرعية والأغاني
    for root, dirs, files in os.walk(MUSIC_DIR):
        for file in files:
            if file.lower().endswith(AUDIO_EXTENSIONS):
                # استخراج المسار النسبي وتحويل الفواصل لتناسب الويب
                relative_path = os.path.join(root, file).replace("\\", "/")
                
                # اسم الأغنية بدون الامتداد
                song_name = os.path.splitext(file)[0]
                
                # اسم المجلد الموجودة فيه الأغنية ليكون التصنيف/القسم
                folder_name = os.path.basename(root)
                if folder_name.lower() == "music":
                    folder_name = "general"

                songs_list.append({
                    "id": len(songs_list) + 1,
                    "name": song_name,
                    "src": relative_path,
                    "category": folder_name,
                    "fav": False,
                    "color": "#38bdf8" # اللون الأزرق السماوي الهادئ المتناسق مع التصميم الجديد
                })

    # كتابة ملف JSON بالترميز العربي الصحيح
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(songs_list, f, ensure_ascii=False, indent=4)

    print(f"🎉 تم بنجاح! تم إنشاء {OUTPUT_JSON} ويحتوي على {len(songs_list)} أغنية جاهزة للعرض! 🚀💙")
else:
    print(f"❌ خطأ: المجلد '{MUSIC_DIR}' غير موجود في مسار المشروع!")