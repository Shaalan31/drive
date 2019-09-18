/**
 *سكربت يستخدم لترتيب القوالب في آخر الصفحة
 * حسب الترتيب الآتي:
 * القوالب الشقيقة
 * قوالب التصفح
 * قوالب الضبط الاستنادي ومعرفات الأصنوفة ومعرفات مركب كيميائي ومصادر طبية
 * شريط البوابات
 * قوالب البذور
 * قوالب المحتوى المختار
 * ثم يرتب التصنيفات حسب الترتيب الأبجدي
 */
 
/**هل الصفحة ضمن نطاق مقالات؟ */
if (mw.config.get('wgNamespaceNumber') === 0 && mw.config.get('wgAction') === "view") {

    /**قائمة القوالب المراد ترتيبها */
    var templates = [];

    /**يمكن تغيير ترتيب الأسطر التالية لتغيير ترتيب القوالب */
    templates.push(".navbox");
	templates.push("#medic-no-res");
    templates.push(".auth-control");
    templates.push(".medic-box");
    templates.push(".chem-box");
    templates.push(".taxon-box");
    templates.push(".bandeau-portail");
    templates.push(".stub");
    templates.push("#fa-box, #ga-box");


    for (var i = 0; i < templates.length; i++) {
        /**جلب القوالب بعد المراجع */
        if ($('div[class^="reflist"]')[0]) {
            sortTemp(true, templates[i]);
        }
        else {
            sortTemp(false, templates[i]);
        }
    }

    function sortTemp(hasRef, temp) {

        var selector;
        (hasRef ? selector = $("div[class^= 'reflist']").nextAll(temp) : selector = $(temp));
        selector.insertBefore("#catlinks");
    }

    /**
     * ترتيب التصنيفات أبجديا
     */
    var mylist = $('#mw-normal-catlinks ul');
    var listitems = mylist.children('li').get();
    var sameTitleCats = [];
    var otherCats = [];

    $.each(listitems, function () {
        if ($(this).find("a").text().startsWith(mw.config.get('wgTitle').replace("_"," "))) {
            sameTitleCats.push($(this));
        }
        else {
            otherCats.push($(this));
        }
    });

    otherCats.sort(function (a, b) {
        return $(a).text().toUpperCase().localeCompare($(b).text().toUpperCase());
    });

    mylist.empty().append(sameTitleCats);
    mylist.append(otherCats);
}