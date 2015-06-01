REG.MODELS.Encumbrance = Backbone.Model.extend({
    urlRoot:"/api/v1/encumbrance",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var Encumbrance = Backbone.Collection.extend({
	model: REG.MODELS.Encumbrance,
	url : '/api/v1/encumbrance',
});

REG.COLLECTIONS.Encumbrance = new Encumbrance;

REG.VIEWS.ExampleListItemEncumbrance = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>#:</b> <%- NStatement %> <b>Тип:</b> <%- TypeOfEncumbrance[\"Name\"] %> <b>Вид:</b> <%- ViewEncumbrance[\"Name\"] %> <b>Дата:</b> <%- Date %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteEncumbrance(<%- id %> )\">Видалити</button><a class=\"btn\" href=\"/edit/<%- id%>/\">Редагувати</a></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

REG.VIEWS.ExampleListEnc = Backbone.View.extend({
	el : "#enc-list",
	initialize : function(options){
	},
	init : function(){
		    this.listenTo(REG.COLLECTIONS.Encumbrance, 'reset', this.addAll, this);

	},
	addOne : function(model) {
		    var view = new REG.VIEWS.ExampleListItemEncumbrance ({ model : model })

		this.$el.append(view.render().el)
	},
	addAll : function(){
		var that = this;
            REG.COLLECTIONS.Encumbrance.each(function(model){
                that.addOne(model);
            });
	},
	remove: function() {
        this.$el.children().remove();
    },
	render : function() {
		this.$el.html(this.template());
		return this;
	}
});

/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
// Object

REG.MODELS.ObjectE = Backbone.Model.extend({
    urlRoot:"/api/v1/object",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var ObjectE = Backbone.Collection.extend({
	model: REG.MODELS.ObjectE,
	url : '/api/v1/object',
});

REG.COLLECTIONS.ObjectE = new ObjectE;

// Document
REG.MODELS.DocumentBase = Backbone.Model.extend({
    urlRoot:"/api/v1/documentbase",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var DocumentBase = Backbone.Collection.extend({
	model: REG.MODELS.DocumentBase,
	url : '/api/v1/documentbase',
});

REG.COLLECTIONS.DocumentBase = new DocumentBase;


// Term

REG.MODELS.Terms = Backbone.Model.extend({
    urlRoot:"/api/v1/terms",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var Terms = Backbone.Collection.extend({
	model: REG.MODELS.Terms,
	url : '/api/v1/terms',
});

REG.COLLECTIONS.Terms = new Terms;
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////

function saveEncumbrance() {
    var i = 0;
    var arrW = [];
    while (i < document.forms.formE[7].length) {
        if(document.forms.formE[7][i].selected) {
            var model = new REG.MODELS.Person({id: document.forms.formE[7][i].value});
            model.fetch({wait: true});
            arrW.push(model);
        }
      i++;
    }

    i = 0;
    var arrS = [];
    while (i < document.forms.formE[8].length) {
        if(document.forms.formE[8][i].selected) {
            var model = new REG.MODELS.Person({id: document.forms.formE[8][i].value});
            model.fetch({wait: true});
            arrS.push(model);
        }
      i++;
    }

    var typeE = null;
    if(document.forms.formE[2].value>0) {
        typeE = new REG.MODELS.TypeEncModel({id: document.forms.formE[2].value});
        typeE.fetch({wait: true});
    }

    var typeR = null;
    if(document.forms.formE[3].value>0) {
        typeR = new REG.MODELS.TypeReg({id: document.forms.formE[3].value});
        typeR.fetch({wait: true});
    }

    var viewE = null;
    if(document.forms.formE[4].value>0) {
        viewE = new REG.MODELS.ViewEncModel({id: document.forms.formE[4].value});
        viewE.fetch({wait: true});
    }

     var o = saveO();
     var d = saveD();
     var t = saveT();


    var enc = new REG.MODELS.Encumbrance(   {NStatement:document.forms.formE[0].value,
                                            DateStatement:document.forms.formE[1].value,
                                            TypeOfEncumbrance:typeE,
                                            TypeReg:typeR,
                                            ViewEncumbrance:viewE,
                                            Date:document.forms.formE[5].value,
                                            AddedInfo:document.forms.formE[6].value,
                                            WPerson:arrW,
                                            SPerson:arrS,
                                            Obj:o,
                                            DocBase:d,
                                            Term:t});

   saveE(enc);
};

function saveE(enc){
     enc.save(null, {
          success: function(model, response){
            document.forms.formE.reset();
            document.forms.formO.reset();
            document.forms.formD.reset();
            document.forms.formT.reset();
          },
          error:function(){
          saveE(enc);
          },
        wait:true
        });
}

function saveO() {
    var obj = null;
    if(document.forms.formO[0].value!="" ||
    document.forms.formO[1].value!="" ||
    document.forms.formO[3].value!=""){
        // Зберігаємо об'єкт
    obj = new REG.MODELS.ObjectE(    {Name:document.forms.formO[0].value,
                                        SerialNumber:document.forms.formO[1].value,
                                        RegNumber:document.forms.formO[2].value,
                                        AddedInfoForUNMovable:document.forms.formO[3].value});
    }

    return obj;
}

function saveD() {
    var doc = null;
    if(document.forms.formD[0].value!="" ||
    document.forms.formD[1].value!="" ||
    document.forms.formD[2].value!="" ||
    document.forms.formD[3].value!=""){
        // Зберігаємо об'єкт
    doc = new REG.MODELS.DocumentBase(  {Name:document.forms.formD[0].value,
                                            Number:document.forms.formD[1].value,
                                            Date:document.forms.formD[2].value,
                                            PublisherName:document.forms.formD[3].value});
    }
    return doc;
}

function saveT() {
    var term = null;
    if(
    document.forms.formT[0].value!=null){
        // Зберігаємо об'єкт

    var tc = null;
    if(document.forms.formT[3].value>0) {
        tc = new REG.MODELS.TypeOfCurrency({id: document.forms.formT[3].value});
        tc.fetch();
    }

    term = new REG.MODELS.Terms(  {SizeObligations:document.forms.formT[0].value,
                                        LimitDate:document.forms.formT[1].value,
                                        AddedInfo:document.forms.formT[2].value,
                                        TypeOfCurrency:tc});

    }
    return term;
}

function deleteEncumbrance(i) {
    var enc = new  REG.MODELS.Encumbrance({id: i});
    enc.fetch({wait:true});

    enc.destroy({
          success: function(model, response){
            console.log('success');
            view.remove();
            REG.COLLECTIONS.Encumbrance.fetch({ reset : true });
          }
        });
};

var enc = null;
var obj = null;
var doc = null;
var term = null;

function editEncumbrance(i) {
    // Отримуємо всі елементи обтяження
    enc = new  REG.MODELS.Encumbrance({id:i});
    obj = null;
    doc = null;
    term = null;
    enc.fetch({
    success: function() {

        obj = enc.get("Obj");
        doc = enc.get("DocBase");
        term = enc.get("Term");
        if(obj!=null){
            document.forms.formO[0].value = obj["Name"];
            document.forms.formO[1].value = obj["SerialNumber"];
            document.forms.formO[2].value = obj["RegNumber"];
            document.forms.formO[3].value = obj["AddedInfoForUNMovable"];
        }
        if(doc!=null){
            document.forms.formD[0].value = doc["Name"];
            document.forms.formD[1].value = doc["Number"];
            document.forms.formD[2].value = doc["Date"];
            document.forms.formD[3].value = doc["PublisherName"];
        }
        if(term!=null){

            document.forms.formT[0].value = term["SizeObligations"];
            document.forms.formT[1].value = term["LimitDate"];
            document.forms.formT[2].value = term["AddedInfo"];

            if(term["TypeOfCurrency"]!=null)
            {
                var arr = term["TypeOfCurrency"].split("/");
                document.forms.formT[3].value = parseInt(arr[arr.length - 2]);
            } else {
                document.forms.formT[3].value = 0;
            }
        }

            // Потрібно засунути це все у форму
         document.forms.formE[0].value = enc.get("NStatement");
         document.forms.formE[1].value = enc.get("DateStatement");
        if(enc.get("TypeOfEncumbrance")!=null)
        {
            var json = JSON.stringify(enc.get("TypeOfEncumbrance"));
            var jsonObj = JSON.parse(json);
            document.forms.formE[2].value = jsonObj["id"];
        } else {
            document.forms.formE[2].value = 0
        }

        if(enc.get("TypeReg")!=null)
        {
            var json = JSON.stringify(enc.get("TypeReg"));
            var jsonObj = JSON.parse(json);
            document.forms.formE[3].value = jsonObj["id"];
        } else {
            document.forms.formE[3].value = 0
        }

        if(enc.get("ViewEncumbrance")!=null)
        {
            var json = JSON.stringify(enc.get("ViewEncumbrance"));
            var jsonObj = JSON.parse(json);
            document.forms.formE[4].value = jsonObj["id"];
        } else {
            document.forms.formE[4].value = 0
        }

         document.forms.formE[5].value = enc.get("Date");
         document.forms.formE[6].value = enc.get("AddedInfo");
        var wp = enc.get("WPerson");
         var i=0;
         var n = wp.length;
         var wper = [];
         while(i<n) {
            var json = JSON.stringify(wp[i]);
            var jsonObj = JSON.parse(json);
            wper.push(jsonObj["id"]);
             i++;
         }


        var i = 0;
        while (i < document.forms.formE[7].length) {

            var j=0;
            while(j<n){
                if(document.forms.formE[7][i].value == wper[j])
                document.forms.formE[7][i].selected = true;
                j++;
            }
          i++;
        }
         /////////////////////////////
         var sp = enc.get("SPerson");
         i=0;
         n = sp.length;
         var sper = [];
         while(i<n) {
            var json = JSON.stringify(sp[i]);
            var jsonObj = JSON.parse(json);
            sper.push(jsonObj["id"]);
             i++;
         }
        var i = 0;
        while (i < document.forms.formE[8].length) {

            var j=0;
            while(j<n){
                if(document.forms.formE[8][i].value == sper[j])
                document.forms.formE[8][i].selected = true;
                j++;
            }
          i++;
        }

        },
    wait:true
    });


};

////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////

function saveEEncumbrance() {
    var i = 0;
    var arrW = [];
    while (i < document.forms.formE[7].length) {
        if(document.forms.formE[7][i].selected) {
            var model = new REG.MODELS.Person({id: document.forms.formE[7][i].value});
            model.fetch({wait: true});
            arrW.push(model);
        }
      i++;
    }

    i = 0;
    var arrS = [];
    while (i < document.forms.formE[8].length) {
        if(document.forms.formE[8][i].selected) {
            var model = new REG.MODELS.Person({id: document.forms.formE[8][i].value});
            model.fetch({wait: true});
            arrS.push(model);
        }
      i++;
    }

    var typeE = null;
    if(document.forms.formE[2].value>0) {
        typeE = new REG.MODELS.TypeEncModel({id: document.forms.formE[2].value});
        typeE.fetch({wait: true});
    }

    var typeR = null;
    if(document.forms.formE[3].value>0) {
        typeR = new REG.MODELS.TypeReg({id: document.forms.formE[3].value});
        typeR.fetch({wait: true});
    }

    var viewE = null;
    if(document.forms.formE[4].value>0) {
        viewE = new REG.MODELS.ViewEncModel({id: document.forms.formE[4].value});
        viewE.fetch({wait: true});
    }

    saveEO();
   saveED();
    saveET();

    enc.set(   {NStatement:document.forms.formE[0].value,
                                            DateStatement:document.forms.formE[1].value,
                                            TypeOfEncumbrance:typeE,
                                            TypeReg:typeR,
                                            ViewEncumbrance:viewE,
                                            Date:document.forms.formE[5].value,
                                            AddedInfo:document.forms.formE[6].value,
                                            WPerson:arrW,
                                            SPerson:arrS,
                                            Obj:obj,
                                            DocBase:doc,
                                            Term:term});
    enc.save(null, {
            type: 'PUT',
          success: function(model, response){
            document.forms.formE.reset();
          },
        wait:true
        });
};

function saveEO() {
    if(document.forms.formO[0].value!="" ||
    document.forms.formO[1].value!="" ||
    document.forms.formO[3].value!=""){
        // Зберігаємо об'єкт
        obj = new REG.MODELS.ObjectE({id:obj["id"]});
        obj.fetch({wait:true});
    obj.set(    {Name:document.forms.formO[0].value,
                                        SerialNumber:document.forms.formO[1].value,
                                        RegNumber:document.forms.formO[2].value,
                                        AddedInfoForUNMovable:document.forms.formO[3].value});
    obj.save(null, {
            type: 'PUT',
          success: function(model, response){
            console.log('success SAVE OBJECT');
            document.forms.formO.reset();
          },
          error: function(){
          saveEO();
          }
        });
    }
}

function saveED() {
    if(document.forms.formD[0].value!="" ||
    document.forms.formD[1].value!="" ||
    document.forms.formD[2].value!="" ||
    document.forms.formD[3].value!=""){
        // Зберігаємо об'єкт
        doc = new REG.MODELS.DocumentBase({id:doc["id"]});
        doc.fetch({wait:true});
    doc.set(  {Name:document.forms.formD[0].value,
                                            Number:document.forms.formD[1].value,
                                            Date:document.forms.formD[2].value,
                                            PublisherName:document.forms.formD[3].value});
    doc.save(null, {
            type: 'PUT',
          success: function(model, response){
            console.log('success SAVE doc');
            document.forms.formD.reset();
          },
          error: function(){
          saveED();
          }
        });
    };
}

function saveET() {
    if(document.forms.formT[0].value!=null ||
    document.forms.formT[1].value!="" ||
    document.forms.formT[2].value!="" ||
    document.forms.formT[3].value!=""){
        // Зберігаємо об'єкт

    var tc = null;
    if(document.forms.formT[3].value>0) {
        tc = new REG.MODELS.TypeOfCurrency({id: document.forms.formT[3].value});
        tc.fetch();
    }
     term = new REG.MODELS.Terms({id:term["id"]});
        term.fetch({wait:true});
    term.set(  {SizeObligations:document.forms.formT[0].value,
                                        LimitDate:document.forms.formT[1].value,
                                        AddedInfo:document.forms.formT[2].value,
                                        TypeOfCurrency:tc});


    term.save(null, {
            type: 'PUT',
          success: function(model, response){
            console.log('success SAVE term');
            document.forms.formT.reset();
          },
          error: function(){
          saveET();
          }
        });
    };
}