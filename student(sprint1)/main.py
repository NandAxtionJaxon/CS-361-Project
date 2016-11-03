#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import random
import os
import urllib
import jinja2

file = open('question.txt', 'r')

subjects = []
questions = []
answers = []
theQuestion = ""
theAnswer = ""
msgfile=[]

def writeMsg():

    file=open('msgFile','a')
    file.write(self.msgfile[0])
    file.write(self.msgfile[1])



for line in file:
    lines = line.split('{}')
    subjects.append(lines[0])
    questions.append(lines[1])
    answers.append(lines[2])

# subject = []

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/page'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('StudentsPage.html')
        self.response.write(template.render())

class MessageHandler(webapp2.RequestHandler):

    def post(self):
        subj = self.request.get('subject')
        ques = self.request.get('question')
        self.msgfile.append(subj)
        self.msgfile.append(ques)
        self.writeMsg()
        self.redirect('/')





class InboxPageGet(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('inboxPage.html')
        template_values = {
            's': subjects,
            'q': questions,
            'a': answers

        }
        self.response.write(template.render(template_values))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('inboxPage.html')

        num = self.request.get('subjectButton')

        """if num == subjects[0]:
    theQuestion = questions[0]
    theAnswer = answers[0]
elif num == subjects[1]:"""

       # theQuestion = questions[int(num)]
        #theAnswer = answers[int(num)]



        template_values = {
            's': subjects,
            'q': questions,
            'a': answers,
            'tq':theQuestion,
            'ta':theAnswer,
            'num': num
            }
        self.response.write(template.render(template_values))




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/inbox', InboxPageGet),
    ('/send',MessageHandler)

], debug=True)


file.close()