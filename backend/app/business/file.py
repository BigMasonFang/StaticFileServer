import zipfile
from io import BytesIO
import asyncio

from app.utils.oss.oss_base import OSSBase


class FileBusiness(OSSBase):
    @classmethod
    async def store_zip_bytes(cls, file: bytes, filename: str):
        '''store user upload .zip http bytes to OSS'''
        file = BytesIO(file)
        # open the bytesIo
        with zipfile.ZipFile(file) as zip:
            # loop the result
            async for zipinfo in zip.infolist():
                with zip.open(zipinfo) as file:
                    # check if it is a dir
                    if zipinfo.is_dir():
                        continue
                    if zipinfo.filename.endswith('DS_Store'):
                        continue

                    # error encode fix
                    new_filename = filename + '/' + zipinfo.filename.encode(
                        'cp437').decode('utf8')

                    # put filename and file to task list
                    await asyncio.create_task(
                        cls.upload_file_cb(new_filename, file))

        return 'ok'

    @classmethod
    async def upload_file_cb(cls, filename, file):
        file_read = file.read()
        result = OSSBase.upload_file(filename, file_read)
