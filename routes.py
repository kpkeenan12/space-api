from flask import Blueprint, Response, request
from ccsds_ndm.ndm_io import NdmIo

cdm_api = Blueprint("cdm_api", __name__)

@cdm_api.route("/cdm", methods=["POST"])
def accept_cdm():
    file = request.files['file']
    cdm = NdmIo().from_bytes(file.stream.read())
    return Response("Accepted", status=202)
