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
import time
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
msglist = []

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/page'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('StudentsPage.html')
        self.response.write(template.render())


class MessageHandler(webapp2.RequestHandler):
    def post(self):
        subj = self.request.get('subject')
        msg = self.request.get('question')
        subjects.append(subj)
        questions.append(msg)
        self.response.write("The message was successfully sent..." + '</br>')
        self.response.write("You will be redirected to the student page in 5 seconds")
        self.response.write("""<head runat="server">
    <meta http-equiv="Refresh" content="5;url='/'" />
</head>""")


class InboxPageGet(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('inboxPage.html')
        template_values = {
            's': subjects,
            'q': questions,
            'a': answers

        }
        self.response.write(template.render(template_values))

class InboxPageMsg(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('inboxPage.html')
        val = self.request.get("subjectButton")
        theQuestion=questions[int(val)-1]

        template_values = {
            's': subjects,
            'q': questions,
            'a': answers,
            'tq':theQuestion
        }
        self.response.write(template.render(template_values))





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/inbox', InboxPageGet),
    ('/send', MessageHandler),
    ('/inboxMsg',InboxPageMsg)

], debug=True)

file.close()
