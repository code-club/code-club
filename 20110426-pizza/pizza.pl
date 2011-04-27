contient(classique, [origan]).
contient(reine, [champignon,jambon]).
contient(campione, [champignon,viande_hachee]).
contient(torino, [jambon, oeuf]).

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
