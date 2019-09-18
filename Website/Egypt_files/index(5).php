/* Any JavaScript here will be loaded for all users on every page load. */
// سكربت تجريبي لإضافة التوقيع تلقائياً عند نسيانه 
//التأكد أن عدد تعديلات المستخدم أقل من 1000 تعديل|، وأنه يحرر في نطاق نقاش المستخدم
if ((mw.config.get( 'wgNamespaceNumber' ) % 2) == 1 && mw.config.get( 'wgUserEditCount' ) < 1000 && $('#wpTextbox1').length > 0) {
    var content = $('#wpTextbox1').val().trim(); // نص التعديل
    
    if ((content.endsWith("ع م)"))){
	    $('#wpSave').click(function() {
	        if ((!content.endsWith("\~\~\~") && (!content.endsWith("ع م)")))){
	            $('#wpTextbox1').val($('#wpTextbox1').val().trim() + "--\~\~\~\~"); //إضافة التوقيع
	        }
	   });
   }
   else if ($("h1#firstHeading").text().includes ("إنشاء ")){
   		$('#wpSave').click(function() {
	        if ((!content.endsWith("\~\~\~"))){
	            $('#wpTextbox1').val($('#wpTextbox1').val() + ".--\~\~\~\~"); //إضافة التوقيع
	        }
	   });
   }
}