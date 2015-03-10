#!/usr/bin/python
#using new package
import sys, os, MySQLdb, SocketServer, SimpleHTTPServer, urllib, urlparse

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                #date1 = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('date1', 'err')
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
		if date1 != 'err':
			output = do_the_big_query(date1[0])
			if len(output) < 1:
				self.wfile.write('NO DIFFS')
			else:
				self.wfile.write(output)
		f.close
                self.finish()

def do_the_big_query(date1):
	con = MySQLdb.connect(host="localhost",user="",passwd="",db="cm")
	cur = con.cursor()
	query = "SELECT switch_id FROM control.switch_id WHERE switch = '" + switch + "' LIMIT 1"
	output = ""
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		table_no = row[0]
		if table_no != prev_table:
	return output

httpd = SocketServer.ThreadingTCPServer(('', 3010), myHandler)
httpd.serve_forever()
