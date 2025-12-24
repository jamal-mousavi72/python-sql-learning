import pyodbc

# تنظیمات اتصال
# نقطه (.) یعنی کامپیوتر خودم
SERVER = r'.\SQLEXPRESS'
DATABASE = 'SchoolDB'

# چک کردن درایورهای نصب شده روی ویندوز
drivers = [x for x in pyodbc.drivers() if 'ODBC Driver' in x]
if not drivers:
    # اگر درایور جدید نبود، از درایور قدیمی ویندوز استفاده کن
    driver_name = 'SQL Server'
else:
    # معمولاً آخرین نسخه رو انتخاب می‌کنیم (مثلاً نسخه 17 یا 18)
    driver_name = drivers[-1]

print(f"Using Driver: {driver_name} 🛠")

# ساختن رشته اتصال (Connection String)
# Trusted_Connection=yes یعنی از یوزرنیم ویندوز استفاده کن (رمز نمی‌خواد)
conn_str = (
    f'DRIVER={{{driver_name}}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'  # برای جلوگیری از ارور SSL
)

try:
    print("Connecting to SQL Server... ⏳")
    # تلاش برای اتصال
    conn = pyodbc.connect(conn_str)

    print("Successfully connected to SchoolDB! 🎉✅")
    print("Database is ready for commands.")

    # بستن اتصال (خیلی مهمه!)
    conn.close()

except pyodbc.Error as e:
    print("❌ Connection Failed!")
    print(f"Error: {e}")
