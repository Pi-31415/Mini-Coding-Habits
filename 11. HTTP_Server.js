var server = http.createServer(function(request,response) {
	function getPostParams(request, callback) {
	    var qs = require('querystring');
	    if (request.method == 'POST') {
	        var body = '';

	        request.on('data', function (data) {
	            body += data;
	            if (body.length > 1e6)
	                request.connection.destroy();
	        });

	        request.on('end', function () {
	            var POST = qs.parse(body);
	            callback(POST);
	        });
	    }
	}
    // in-server request from PHP
    if (request.method === "POST") {
    	getPostParams(request, function(POST) {	
			messageClients(POST.data);
			response.writeHead(200);
			response.end();
		});
		return;
	}
});
server.listen(8080);
