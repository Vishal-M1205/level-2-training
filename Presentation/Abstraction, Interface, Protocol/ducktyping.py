class LocalStorage:
    def save(self, filename: str):
        print(f"Saving {filename} locally")


class CloudStorage:
    def save(self, filename: str):
        print(f"Uploading {filename} to cloud")


def upload_file(storage):
    storage.save("report.pdf")


local = LocalStorage()
cloud = CloudStorage()

upload_file(local)
upload_file(cloud)
