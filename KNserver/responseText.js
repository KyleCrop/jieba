function readTextFile(file)
		{
			var rawFile = new XMLHttpRequest();
			rawFile.open("GET", file, true);
			rawFile.onreadystatechange = function ()
			{
				alert(rawFile.readyState);
				if(rawFile.readyState === 4)
				{
					alert(rawFile.status);
				    if(rawFile.status === 200 || rawFile.status == 0)
				    {
				    	alert(rawFile.responseText);
				        var allText = rawFile.responseText;
				        alert(allText);
				    };
				};
			};
			rawFile.send(null);
		};
	  
	  //var xmlhttp = "view-source:https://www.google.com.hk/?gfe_rd=cr&ei=XZfDU7P6L6uJ8QexrYCwDQ";
	  //var xmlhttp = "view-source:http://www.baixing.com/?changeLocation=yes";
	  var xmlhttp = "file:///home/kyle/Documents/jieba/KNserver/Baixing_citySourceCode.txt";
	  readTextFile(xmlhttp);
		  
