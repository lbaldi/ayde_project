# - coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import smtplib

class emailSender(object):

    @classmethod
    def send_email(cls, smtp, port, email, password, recipient, subject, body):

        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (email, ", ".join(TO), SUBJECT, TEXT)

        # PARA DESACTIVAR SEGURIDAD DE GOOGLE
        #https://www.google.com/settings/security/lesssecureapps

        server = smtplib.SMTP(smtp, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipient, message)
        server.close()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: