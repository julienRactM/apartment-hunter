#### **the presentation_requirements.txt file must be installed first**
##### Commands to run to open the presentation :

``jupyter nbconvert --to slides Présentation/Présentation_notebook.ipynb --post serve``

##### Commands to run to open the presentation :

``jupyter nbconvert --to pdf Présentation/Présentation_notebook.ipynb``

##### Commande to do both

``jupyter nbconvert --to pdf Présentation/Présentation_notebook.ipynb | jupyter nbconvert --to slides Présentation/Présentation_notebook.ipynb --post serve``
