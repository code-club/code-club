contient(classique, [origan]).
contient(reine, [champignon,jambon]).
contient(campione, [champignon,viande_hachee]).
contient(torino, [jambon, oeuf]).
contient(exotique,[jambon,ananas]).
contient(paysanne,[lardon, oeuf]).
contient(calzoneSoufflee,[jambon, oeuf]).
contient(fromagereSoufflee,[brie, gorgonzola, chèvre]).
contient(neptuneSoufflee,[thon, olive, oeuf]).
contient(napolitaine,[anchoi, capre, olive]).
contient(quatrefromages,[brie, gorgonzola, chevre]).
contient(quatrejambons,[jambon, lardon, pepperoni, chorizo]).
contient(miami,[poulet, poivron, oignon]).
contient(orientale,[merguez, oignon, poivron, oeuf]).
contient(americaine,[bacon, oignon, oeuf, cremeFraiche]).
contient(aliBaba,[thon, oignon, poivron, oeuf]).
contient(topPizza,[jambon, lardon, pepperoni, oeuf]).
contient(pizzaChef,[merguez, viandeHachee, oignon]).
contient(sicilienne,[jambon, chorizo, champignon, viandeHachee]).
contient(vulcano,[chevre, anchoi, tomateFraiche]).
contient(fruitsDeMer,[fdm, ail, persil, citron]).
contient(texas,[viandeHachee, merguez, chorizo, poivron]).
contient(sardenia,[poulet, mozzarella, chevre]).
contient(vegetarienne,[poivron, oignon, artichaut, champignon, tomateFraiche, olive]).
contient(quatreSaisons,[jambon, champignon, artichaut, olive]).
contient(forestiere,[champignon, lardon, cremeFraiche]).
contient(fermiere,[poulet, pommeDeTerre, oeuf]).
contient(royale,[viandeHachee, oignon, pommeDeTerre, chevre]).
contient(palerma,[jambon, merguez, champignon, oeuf]).
contient(romaine,[jambon, merguez, viandeHachee, chorizo, oeuf]).
contient(bouchere,[viandeHachee, oignon, oeuf, cremeFraiche]).
contient(enrique,[jambon, chevre, oignon, tomateFraiche, olive]).
contient(pizzaKebab,[viandeGrecque, tomateFraiche, oignon]).
contient(western,[chevre, lardon]).
contient(provencale,[poulet, tomateFraiche, oignon]).

isIngredientDe(P,I) :- contient(P, R), member(I,R).

% degeu(champignon).
degeu(tasoeur).

pizza(X) :- contient(X,_).
ingredient(Y) :- isIngredientDe(_,Y).

immangeable(P) :- isIngredientDe(P, I), degeu(I).
acceptable(P) :- pizza(P),not(immangeable(P)).

pizza_differente(P1, P2) :- P1 \= P2, contient(P1, R), contient(P2, S),forall(member(El,R), not(member(El,S))).
ingredient_different(_, []).
ingredient_different(P1, [P2|R]) :- pizza(P2), pizza_differente(P1, P2), ingredient_different(P1, R).

menu([]).
menu([P|R]) :- acceptable(P), ingredient_different(P, R), menu(R).
