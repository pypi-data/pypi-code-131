# Copyright 2022 UpshotAPPS

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
   
from os.path import exists
import json

class guardedsettings:

	def __init__( self ):
	
		self.filename = "guardedsettings.json"
		self.SettingsDictionary = {}
		if exists(self.filename):
			with open(self.filename, "r") as readFile:
				self.SettingsDictionary = json.loads(readFile.read())
		else:
			with open(self.filename, "w") as writeFile:
				writeFile.write(json.dumps(self.SettingsDictionary))
