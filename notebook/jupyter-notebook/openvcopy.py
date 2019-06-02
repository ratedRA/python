from openvino import inference_engine as ie
from openvino.inference_engine import IENetwork, IEPlugin
model_xml = './FP32/face-detection-retail-0004.xml'
model_bin = './FP32/face-detection-retail-0004.bin'
plugin_dir = None
import os
import cv2
import numpy as np
assert 'computer_vision_sdk' in os.environ['PYTHONPATH']
OPENVINO_CPU_SO = 'FP32/lib/libcpu_extension.so'

plugin = IEPlugin("CPU", plugin_dirs=plugin_dir)
net = IENetwork.from_ir(model=model_xml, weights=model_bin)

input_blob = next(iter(net.inputs))
out_blob = next(iter(net.outputs))
plugin.add_cpu_extension(OPENVINO_CPU_SO)

exec_net = plugin.load(network=net)
del net

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
while 1:
	ret, img = cap.read()
	print(img.shape)

	img = cv2.resize(img, (300, 300), interpolation = cv2.INTER_LINEAR) 
	print(img.shape)
	img2 = np.moveaxis(img, -1, 0)
	img2=np.reshape(img2,(1,3,300,300))
	#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	res = exec_net.infer(inputs={input_blob: img2})
	output_node_name = list(res.keys())[0]
	res = res[output_node_name]
	print(res[0][0][0][3:])
	print(res.shape)
	#break
	x,y,w,h=res[0][0][0][3:]
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	

	# for (x,y,w,h) in res[0][0][0][3:]:
	# 	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	# 	roi_color = img[y:y+h, x:x+w]
	# img = np.moveaxis(img, -1, 0)
	# img=np.reshape(img,(300,300,3))
	# print(img.shape)
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
