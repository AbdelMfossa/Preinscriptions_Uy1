from django import forms



class CivilForm(forms.Form):    
    """ forms pour l'état civil """

    #Les listes des menus déroulants pour l'état civil de l'étudiant
    listesexe = [('féminin','Féminin'),('masculin','Masculin')]
    listestatutmarital = [('célibataire','Célibataire'),('marié','Marié'),('divorcé','Divorcé')]
    listepremierelangue = [('français','Français'),('anglais','Anglais')]
    listestatutprofessionnel = [('0',' '),('sansemploi','Sans emploi'),('autoentrepreneur','Auto-entrepreneur'),
                                ('Salarié','salarié')]
    listegrade = [('0',' '),('professeur','Professeur'),('maitreconf','Maître de Conférence'),
                                ('chargecours','Chargé de Cours'),('autre','Autres')]
    listeechelon = [('0',' '),('1','1'),('2','2'),('3','3'),('4','4')]
    #-----------------------------------------------------------------------------------------------------------
    prenom = forms.CharField(label="Prénom", max_length=100, required=True)
    nom = forms.CharField(label="Nom", max_length=100, required=True)
    datenaissance = forms.DateField(label="Date de naissance", widget=forms.TextInput(attrs={'type': 'date'}),required=True)
    lieunaissance = forms.CharField(label="Lieu de naissance", max_length=100, required=True)
    numerocni = forms.CharField(label="Numéro de CNI", max_length=100, required=False)
    sexe = forms.CharField(label="Sexe", widget=forms.Select(choices=listesexe), required=True)
    adresse = forms.CharField(label="Adresse", max_length=100, required=True)
    telephone = forms.CharField(label="Téléphone", max_length=100, required=True)
    email = forms.EmailField(label="Votre adresse e-mail", help_text="exemple: accueil@univ-yaounde1.cm", required=True)
    statutmarital = forms.CharField(label="Statut marital",  widget=forms.Select(choices=listestatutmarital), required=True)
    premierelangue = forms.CharField(label="Première langue", widget=forms.Select(choices=listepremierelangue), required=True)
    statutprofessionnel = forms.CharField(label="Statut professionnel", widget=forms.Select(choices=listestatutprofessionnel), 
                            required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    lieudujob = forms.CharField(label="Lieu de votre emploi", max_length=100, required=False)
    grade = forms.CharField(label="Grade", widget=forms.Select(choices=listegrade), required=False)
    echelon = forms.CharField(label="Echelon", widget=forms.Select(choices=listeechelon), required=False)



class FiliationForm(forms.Form):    
    """ forms pour la filiation de l'étudiant """

    #Les listes des menus déroulants pour les informations de filiation
    listenationalite = [('cameroun','Cameroun'),('congo','Congo'),('gabon','Gabon'),('guinee','Guinnée-équatoriale'),
                        ('centrafique','République Centraficaine'),('tchad','Tchad'),('autre','Autre'),]
    listeregion = [('célibataire','Célibataire'),('marié','Marié'),('divorcé','Divorcé')]
    listedepartement = [('célibataire','Célibataire'),('marié','Marié'),('divorcé','Divorcé')]

    #-----------------------------------------------------------------------------------------------------------
    nationalite = forms.CharField(label="Nationalité", widget=forms.Select(choices=listenationalite), required=True)
    premierelangue = forms.CharField(label="Première langue", widget=forms.Select(choices=listenationalite), required=True)
    premierelangue = forms.CharField(label="Première langue", widget=forms.Select(choices=listenationalite), required=True)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)
    profession = forms.CharField(help_text="Votre profession si vous en avez une.", 
                                label="Profession", max_length=100, required=False)