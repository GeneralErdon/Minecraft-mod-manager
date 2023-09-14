import os
import requests as rq

class ApiRequest:
    
    def __init__(self, end_point:str,  headers:dict[str,str] = None,) -> None:
        self._api_key:str = os.environ.get("CURSEFORGE_API_KEY")
        self._base_url:str = os.environ.get("CURSEFORGE_BASE_URL")
        
        self._end_point = end_point
        self.headers:dict[str,str] = {"x-api-key": self._api_key}
        
        if headers is not None:
            self.headers = {**self.headers, **headers}
    
    @property
    def end_point(self):
        self._end_point = self.__format_endpoint(self._end_point)
        
        return self._end_point
    
    @end_point.setter
    def end_point(self, value:str):
        assert isinstance(value, str), "endpoint must be a str"
        self._end_point = self.__format_endpoint(value)
    
    @property
    def base_url(self):
        return self._base_url
    
    def __format_endpoint(self, txt:str):
        if txt[0] != "/":
            txt = f"/{txt}"
        return txt
    
    def get_url(self):
        return f"{self.base_url}{self.end_point}"
    
    
    def post(self, body:dict[str, str|int], **options):
        
        
        response = rq.post(
            url=self.get_url(),
            data=body,
            headers=self.headers,
            **options
        )
        return response
    
    def get(self, query_params:dict[str, str|int], **options):
        
        response = rq.get(
            url=self.get_url(),
            params=query_params,
            headers=self.headers,
            **options
        )
        
        return
    