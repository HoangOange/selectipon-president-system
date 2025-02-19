from pymongo import MongoClient

# Thay thế bằng connection string của bạn
MONGO_URI = "mongodb+srv://2254810192:<ghostriver003>@election-president-syst.wqzai.mongodb.net/?retryWrites=true&w=majority&appName=election-president-system"

def get_database():
    client = MongoClient(MONGO_URI)
    db = client["election-president-system"]
    return db

if __name__ == "__main__":
    db = get_database()
    print("✅ Kết nối MongoDB thành công!")
    print("Danh sách collections:", db.list_collection_names())
