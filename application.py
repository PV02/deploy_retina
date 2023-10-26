from flask import Flask, render_template, request, jsonify
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps

print(np.sin(5))
