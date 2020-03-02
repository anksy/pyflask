from app.constants.response import (SUCCESSFULL, FAILED)

class Resposne:
    def success(self, msg="", data=None, code=200):
        return {
            "type": "success",
            "message": msg or SUCCESSFULL,
            "data": data
        }, code
    
    def error(self, msg="", error=None, code=400):
        return {
            "type": "error",
            "message": msg or FAILED,
            "error": error
        }, code