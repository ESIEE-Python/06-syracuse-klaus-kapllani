# main.py
"""
author = klaus.kapllani@esiee.fr
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """permet d'afficher le graphique la suite de Syracuse

    Args:
        lsyr : la suite de Syracuse de source n

    Returns:
        rien
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = range(len(lsyr))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [ n ]
    value = n
    # On s'arrête à value = 1, car ensuite la suite boucle (donc inutile)
    while value != 1:
        if value % 2 == 0:
            value = value // 2
        else:
            value = 3*value+1
        l += [ value ]
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # Il n'y a qu'une seule valeur qui est égal à 1, et c'est le dernier élément
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    source = l[0]
    for i, value in enumerate(l):
        if value < source:
            return i
    return 0  # Retourne 0 si la suite ne dépasse jamais la valeur initiale


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    value = 0
    for i in enumerate(l):
        if l[i] > value:
            value = l[value]
    return value

def main():
    """
    Fonction principale qui print la liste de tuple d'abord en itératif,
    puis en récurcif.

    Returns :
        rien
    """

    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
