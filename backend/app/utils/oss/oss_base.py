import oss2


class OSSBase:
    bucket = None

    @classmethod
    def initialize(cls, access_key_id, access_key_secret, endpoint, bucket):
        basic_auth = oss2.Auth(access_key_id, access_key_secret)
        basic_bucket = oss2.Bucket(basic_auth, endpoint, bucket)
        cls.bucket = basic_bucket

    @classmethod
    def upload_file(cls, remote_path, file):
        return cls.bucket.put_object(remote_path, file)

    @classmethod
    def upload_from_file(cls, local_path: str, remote_path: str):
        """上传文件到OSS中
        local_path: 本地文件路径
        remote_path: OSS文件路径"""
        return cls.bucket.put_object_from_file(remote_path, local_path)

    @classmethod
    def get_bukect_iter(cls, **kwargs):
        return oss2.ObjectIteratorV2(cls.bucket, **kwargs)
