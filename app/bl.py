import app.db as db
import dlib
import io
import base64
import os
from imageio import imread
from scipy.spatial import distance


def convert(b64):
    return imread(io.BytesIO(base64.b64decode(b64)))


def check(json_from_request):
    try:
        shape = None
        json_from_db = db.get_employee_photo_base64(json_from_request['id'])
        sp = dlib.shape_predictor(os.path.join('data', 'shape_predictor_68_face_landmarks.dat'))
        facerec = dlib.face_recognition_model_v1(os.path.join('data', 'dlib_face_recognition_resnet_model_v1.dat'))
        detector = dlib.get_frontal_face_detector()

        img = convert(json_from_db['photo'])

        det = detector(img, 1)
        for k, d in enumerate(det):
            shape = sp(img, d)
        face_descriptor1 = facerec.compute_face_descriptor(img, shape)

        img = convert(json_from_request['photo'])

        det = detector(img, 1)
        for k, d in enumerate(det):
            shape = sp(img, d)
        face_descriptor2 = facerec.compute_face_descriptor(img, shape)

        dist = distance.euclidean(face_descriptor1, face_descriptor2)
        result = '{\'error\':\'\',\'result\':' + str(dist < 0.6).lower() + '}'
    except:
        result = '{\'error\':\'Something went wrong\',\'result\':false}'

    return result
