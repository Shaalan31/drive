/*[[قالب:مبوبة]]*/

#tabContainer{
	width: 100%;
	margin: 5px 0;
}

#tabContainer > .tabs{
	height:30px;
	position: relative;
	right: -15px;
	width: 100%;
}

.tabs > ul{
	font-size: 1em;
	list-style:none;
}

.tabs > ul > li{
	padding:1px 5px;
	display:block;
	float:right;
	color:#FFF;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
	border-style: solid;
	border-width: 1px 1px 0px 1px;
	line-height: 1.5em !important;
	font-weight: bold;
	border-color: silver;
}

.tabs > ul > li:hover{
	cursor:pointer;
}

.tabs > ul > li.tabActiveHeader{
	background: #FFFFFF;
	cursor:pointer;
	color: gainsboro;
}

.tabscontent {
	padding:5px 10px;
	margin-top: -5px;
	color:#333;
	background: #FFFFFF;
	border: 1px solid silver;
}