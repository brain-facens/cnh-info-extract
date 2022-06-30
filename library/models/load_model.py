from library.extra_functions import os, re
from library.models import *


class OCR:

    def __init__(self) -> None:
        self.__lang = "en"
        self.__use_ang_cls = True

    def init(self) -> int:
        try:
            self.__ocr = PaddleOCR(use_angle_cls=self.__use_ang_cls, lang=self.__lang)
        except:
            return 0
        else:
            return 1

    def extract_info(self, _document) -> None or dict:
        
        __shape = _document.shape

        __crop = {
            "name":([
                [int(__shape[1]*0.04),int(__shape[0]*0.01),int(__shape[1]*0.7),int(__shape[0]*0.12)],
                [int(__shape[1]*0.02),int(__shape[0]*0.01),int(__shape[1]*0.7),int(__shape[0]*0.08)],
                [int(__shape[1]*0.02),int(__shape[0]*0.01),int(__shape[1]*0.7),int(__shape[0]*0.08)]
            ],r"[A-Za-z ]+"),
            "doc_org_uf":([
                [int(__shape[1]*0.43), int(__shape[0]*0.16), int(__shape[1]*0.73), int(__shape[0]*0.25)],
                [int(__shape[1]*0.43),int(__shape[0]*0.14),int(__shape[1]*0.73),int(__shape[0]*0.22)],
                [int(__shape[1]*0.42),int(__shape[0]*0.12),int(__shape[1]*0.73),int(__shape[0]*0.2)],
                [int(__shape[1]*0.44),int(__shape[0]*0.13),int(__shape[1]*0.75),int(__shape[0]*0.22)],
                [int(__shape[1]*0.45),int(__shape[0]*0.13),int(__shape[1]*0.75),int(__shape[0]*0.23)],
                [int(__shape[1]*0.47),int(__shape[0]*0.13),int(__shape[1]*0.77),int(__shape[0]*0.24)],
                [int(__shape[1]*0.48),int(__shape[0]*0.12),int(__shape[1]*0.78),int(__shape[0]*0.22)],
                [int(__shape[1]*0.44),int(__shape[0]*0.11),int(__shape[1]*0.75),int(__shape[0]*0.2)]
            ],r"[0-9]{8,9} [A-Z]{3}\/?[A-Z]{2}"),
            "cpf":([
                [int(__shape[1]*0.43),int(__shape[0]*0.28),int(__shape[1]*0.73),int(__shape[0]*0.38)],
                [int(__shape[1]*0.43),int(__shape[0]*0.28),int(__shape[1]*0.74),int(__shape[0]*0.37)],
                [int(__shape[1]*0.42),int(__shape[0]*0.26),int(__shape[1]*0.73),int(__shape[0]*0.33)],
                [int(__shape[1]*0.44),int(__shape[0]*0.26),int(__shape[1]*0.75),int(__shape[0]*0.34)],
                [int(__shape[1]*0.46),int(__shape[0]*0.24),int(__shape[1]*0.76),int(__shape[0]*0.33)],
                [int(__shape[1]*0.45),int(__shape[0]*0.25),int(__shape[1]*0.77),int(__shape[0]*0.34)],
                [int(__shape[1]*0.46),int(__shape[0]*0.29),int(__shape[1]*0.76),int(__shape[0]*0.37)]
            ],r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}"),
            "born_day":([
                [int(__shape[1]*0.74),int(__shape[0]*0.28),int(__shape[1]*0.97),int(__shape[0]*0.38)],
                [int(__shape[1]*0.76),int(__shape[0]*0.28),int(__shape[1]*0.99),int(__shape[0]*0.38)],
                [int(__shape[1]*0.74),int(__shape[0]*0.25),int(__shape[1]*0.97),int(__shape[0]*0.33)],
                [int(__shape[1]*0.74),int(__shape[0]*0.27),int(__shape[1]*0.97),int(__shape[0]*0.35)],
                [int(__shape[1]*0.72),int(__shape[0]*0.26),int(__shape[1]*0.95),int(__shape[0]*0.36)],
                [int(__shape[1]*0.73),int(__shape[0]*0.27),int(__shape[1]*0.94),int(__shape[0]*0.38)],
                [int(__shape[1]*0.71),int(__shape[0]*0.29),int(__shape[1]*0.94),int(__shape[0]*0.39)]
            ],r"[0-9]{2}\/[0-9]{2}\/[0-9]{4}"),
            "cat. hab.":([
                [int(__shape[1]*0.84),int(__shape[0]*0.79),int(__shape[1]*0.95),int(__shape[0]*0.86)],
                [int(__shape[1]*0.85),int(__shape[0]*0.81),int(__shape[1]*0.95),int(__shape[0]*0.88)],
                [int(__shape[1]*0.85),int(__shape[0]*0.74),int(__shape[1]*0.95),int(__shape[0]*0.82)],
                [int(__shape[1]*0.84),int(__shape[0]*0.75),int(__shape[1]*0.94),int(__shape[0]*0.83)],
                [int(__shape[1]*0.84),int(__shape[0]*0.77),int(__shape[1]*0.95),int(__shape[0]*0.84)],
                [int(__shape[1]*0.83),int(__shape[0]*0.81),int(__shape[1]*0.93),int(__shape[0]*0.87)],
                [int(__shape[1]*0.85),int(__shape[0]*0.81),int(__shape[1]*0.95),int(__shape[0]*0.87)]
            ],r"[A-Z]{1,2}"),
            "num. reg.":([
                [int(__shape[1]*0.04),int(__shape[0]*0.9),int(__shape[1]*0.4),int(__shape[0]*0.98)],
                [int(__shape[1]*0.04),int(__shape[0]*0.93),int(__shape[1]*0.4),int(__shape[0])],
                [int(__shape[1]*0.04),int(__shape[0]*0.89),int(__shape[1]*0.4),int(__shape[0]*0.98)],
                [int(__shape[1]*0.06),int(__shape[0]*0.89),int(__shape[1]*0.43),int(__shape[0]*0.98)],
                [int(__shape[1]*0.02),int(__shape[0]*0.89),int(__shape[1]*0.42),int(__shape[0]*0.98)],
                [int(__shape[1]*0.05),int(__shape[0]*0.93),int(__shape[1]*0.42),int(__shape[0])],
                [int(__shape[1]*0.05),int(__shape[0]*0.92),int(__shape[1]*0.42),int(__shape[0]*0.99)]
            ],r"[0-9]{11}"),
            "val.":([
                [int(__shape[1]*0.43),int(__shape[0]*0.9),int(__shape[1]*0.68),int(__shape[0]*0.98)],
                [int(__shape[1]*0.43),int(__shape[0]*0.94),int(__shape[1]*0.68),int(__shape[0])],
                [int(__shape[1]*0.43),int(__shape[0]*0.88),int(__shape[1]*0.68),int(__shape[0]*0.97)],
                [int(__shape[1]*0.44),int(__shape[0]*0.9),int(__shape[1]*0.69),int(__shape[0]*0.99)],
                [int(__shape[1]*0.41),int(__shape[0]*0.9),int(__shape[1]*0.66),int(__shape[0]*0.99)],
                [int(__shape[1]*0.42),int(__shape[0]*0.89),int(__shape[1]*0.67),int(__shape[0]*0.98)]
            ],r"[0-9]{2}\/[0-9]{2}\/[0-9]{4}"),
            "frst_hab":([
                [int(__shape[1]*0.71),int(__shape[0]*0.9),int(__shape[1]*0.95),int(__shape[0]*0.98)],
                [int(__shape[1]*0.71),int(__shape[0]*0.94),int(__shape[1]*0.95),int(__shape[0])],
                [int(__shape[1]*0.71),int(__shape[0]*0.88),int(__shape[1]*0.95),int(__shape[0]*0.97)],
                [int(__shape[1]*0.69),int(__shape[0]*0.88),int(__shape[1]*0.93),int(__shape[0]*0.97)],
                [int(__shape[1]*0.73),int(__shape[0]*0.88),int(__shape[1]*0.97),int(__shape[0]*0.97)],
                [int(__shape[1]*0.69),int(__shape[0]*0.9),int(__shape[1]*0.93),int(__shape[0]*0.99)],
                [int(__shape[1]*0.73),int(__shape[0]*0.86),int(__shape[1]*0.97),int(__shape[0]*0.95)]
            ],r"[0-9]{2}\/[0-9]{2}\/[0-9]{4}")
        }

        __data = {}
        for key in __crop.keys():
            for points in __crop[key][0]:
                __x1, __y1, __x2, __y2 = points
                __re = __crop[key][1]
                __value = self.__ocr.text_recognizer([_document[__y1:__y2, __x1:__x2]])[0][0][0]
                if not re.fullmatch(__re, __value) is None:
                    __data[key] = __value
                    break
                __data[key] = None
        return __data

class CNH_Detect:

    def __init__(self) -> None:
        self.__model_name = "cnh.pt"

        __curr_path = os.path.dirname(os.path.realpath(__file__))
        
        self.__model_path = os.path.join(__curr_path,self.__model_name)

    def init(self) -> int:
        # self.__cnh = torch.hub.load("ultralytics/yolov5", "custom", path=self.__model_path, device="cpu")
        # try:
        #     # self.__cnh = torch.hub.load("ultralytics/yolov5", "custom", path=self.__model_path, device="cpu")
        #     pass
        # except:
        #    return 0
        # else:
        #     return 1
        return 1

    def detection(self, _frame) -> None or dict:
        
        __result = self.__cnh(_frame)
        __data = __result.pandas().xyxy[0]
        if __data.shape[0]:
            return {
                "doc":_frame[int(__data["ymin"][0]):int(__data["ymax"][0]), int(__data["xmin"][0]):int(__data["xmax"][0])],
                "class":__data["class"][0],
                "conf":__data["confidence"][0],
                "x1":int(__data["xmin"][0]),
                "y1":int(__data["ymin"][0]),
                "x2":int(__data["xmax"][0]),
                "y2":int(__data["ymax"][0])
            }
        return None
