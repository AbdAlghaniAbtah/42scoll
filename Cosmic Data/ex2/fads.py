def cryptic_sorter(strings):
    # ننشئ دالة فرعية تحسب عدد الحروف المتحركة في الكلمة
    def get_vowel_count(s):
        count = 0
        for char in s.lower():
            if char in 'aeiou':
                count += 1
        return count

    # نستخدم دالة الترتيب sorted
    # الـ key هو المعيار الذي نرتب على أساسه
    # نضع المعايير داخل tuple بالترتيب: (الطول، الكلمة نفسها للأبجدية، عدد المتحركات)
    return sorted(strings, key=lambda s: (len(s), s, get_vowel_count(s)))

# الشرح: عند الترتيب، بايثون تقارن العنصر الأول في الـ tuple، إذا تساووا تنتقل للثاني، وهكذا
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))