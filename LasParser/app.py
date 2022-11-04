import os
import io
from flask import Flask, render_template, request
import json
import lasio as lasio


Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload

class LasInfo():
  def __init__(self, mnemonic, unit,value, descr):
    self.mnemonic = mnemonic
    self.unit = unit
    self.value = value
    self.descr = descr

class ParsedLas():
  Version = []
  Wells = []
  Parameters = []
  Curves = []
  Data = []
  def GetString(self):
    versionString = json.dumps(self.Version, default = self.encoder_LasInfo)
    wellString = json.dumps(self.Wells, default = self.encoder_LasInfo)
    parameterString = json.dumps(self.Parameters, default = self.encoder_LasInfo)
    curveString = json.dumps(self.Curves, default = self.encoder_LasInfo)
    dataString = str(self.Data)
    return "{\"Version\": % s,\"Well\":% s,\"Parameters\": % s,\"Curves\": % s, \"Data\":% s}" % (versionString, wellString, parameterString, curveString, dataString)
  def encoder_LasInfo(self, info):
    if isinstance(info, LasInfo):
      return {'mnemonic':info.mnemonic,'unit':info.unit, 'value':info.value, 'descr':info.descr}



@app.route('/')
def index():
    return "You have reached the LAS parser"

@app.route("/getfile", methods=["POST"])
def getfile():
    file = request.files['file']
    return file.read()

@app.route("/getparsedinfo", methods=["GET"])
def getwells():
    file = request.files['file']
    #file.save(os.path.join(os. getcwd(), file.filename))
    stream = io.StringIO(file.stream.read().decode("ISO-8859-1"), newline=None)
    las = lasio.read(stream)
    p1 = ParsedLas()
    versions = las.version
    for version in versions:
        p1.Version.append(LasInfo(version.mnemonic, version.unit, version.value, version.descr))
    wells = las.well
    for well in wells:
        p1.Wells.append(LasInfo(well.mnemonic, well.unit, well.value, well.descr))
    parameters = las.params
    for parameter in parameters:
        p1.Parameters.append(LasInfo(parameter.mnemonic, parameter.unit, parameter.value, parameter.descr))
    curves = las.curves
    for curve in curves:
        p1.Curves.append(LasInfo(curve.mnemonic, curve.unit, curve.value, curve.descr))
    for x in las.data:
        p1.Data.append(list(x))
    astr = p1.GetString()
    c = astr.replace("nan", "null")
    return c




if __name__ == "__main__":
    app.run(host="0.0.0.0")
