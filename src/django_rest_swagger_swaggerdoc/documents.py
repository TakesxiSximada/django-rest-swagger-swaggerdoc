# -*- coding: utf-8 -*-
import yaml


class SwaggerDoc(dict):
    def load_yaml(self, path):
        with open(path, 'rb') as fp:
            data = yaml.load(fp.read())
            self.update(data)
