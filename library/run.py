from extra_functions import tools
from extra_functions import *

from model import load_model
from model import *


parser = argparse.ArgumentParser()
parser.add_argument("--source", type=int, default=0, help="Entrada da câmera que será utilizada.")
arg = parser.parse_args()


def main(_webcam:int):
    
    # Load models.
    # OCR.
    ocr = load_model.OCR()
    if not ocr.init():
        tools.ERROR("Something went wrong when the OCR model was initializing.")
        return -1
    # CNH detector.
    cnh = load_model.CNH_Detect()
    if not cnh.init():
        tools.ERROR("Something went wrong when the CNH detector model was initializing.")
        return -1

    # Initializing camera.
    cam = cv2.VideoCapture(_webcam)
    _, video = cam.read()
    if not _:
        tools.ERROR("Invalid camera.")
        return -1
    
    is_running = True
    min_conf = 0.8

    # Intro.
    # tools.INTRO()

    # Main application.
    while is_running:
        
        ret, frame = cam.read()
        field = frame.copy()
        height, width, channels = frame.shape

        # Detection.
        result = cnh.detection(frame)

        # Screen.
        if not result is None:
            if result["conf"] >= min_conf:
                cv2.rectangle(frame, (result["x1"], result["y1"]), (result["x2"], result["y2"]), (0,255,0), 1)

        cv2.rectangle(field, (15,15), (210,60), (0,0,0), -1)
        frame = cv2.addWeighted(frame, 0.8, field, 0.2, 1)
        cv2.putText(frame, tools.QUIT_TXT, (20,32), 1, 1, (255,0,255), 2)
        cv2.putText(frame, tools.INFO_TXT, (20,52), 1, 1, (0,255,255), 2)

        cv2.rectangle(frame, (10,10), (width-10, height-10), (0,255,0), 1)
        cv2.imshow("CNH INFO EXTRACT - (BRAIN)", frame)
        key = cv2.waitKey(1)

        if key == tools.QUIT:
            is_running = False
        if key == tools.EXTRACT_INFO and not result is None:
            data = ocr.extract_info(result["doc"])
            tools.print_results(data)
            tools.save_results(data)

    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    status = main(arg.source)
    print("Application final status: " + str(status))
