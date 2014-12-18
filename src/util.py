# -*- coding: utf-8 -*-

import os
import json


class Settings:

  def __init__(self):
    path = os.path.expanduser('~/.jaylen/')
    cfg = 'config.json'
    if not os.path.exists(path):
      os.makedirs(path)
    with open(os.path.join(path, cfg)) as config:
      self.settings = json.loads(config)

