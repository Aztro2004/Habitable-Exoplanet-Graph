from django.shortcuts import render  # modulo para renderizar htmls
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import math
from random import randint

from django.shortcuts import get_object_or_404
from .models import Exoplanet

# Create your views here.

# request de vistas
def home(request):
    return render(request,'index.html')

def galeria(request):
    R = [randint(1,66) for i in range(4)]
    c = 0
    for r in R:
        exo = get_object_or_404(Exoplanet, id=r)
        Sun_planet_orb(
            f"Exoplanets_web/static/img/images/demo/Exoplanets/random({c})",
            exo.pl_name,
            exo.pl_rade,
            exo.st_rad,
            exo.pl_orbsmax,
        )
        c+=1
    return render(request,'gallery.html')

def todos(request):
    return render(request,'full-width.html')


def catalogue(request,ind):
    exo = get_object_or_404(Exoplanet, id=ind)
    Sun_planet_orb(
        "Exoplanets_web/static/img/images/demo/Exoplanets/actual1",
        exo.pl_name,
        exo.pl_rade,
        exo.st_rad,
        exo.pl_orbsmax,
    )
    context = {
        "data": {
            "pl_name": exo.pl_name,
            "pl_rade": exo.pl_rade,
            "st_rad": exo.st_rad,
            "pl_orbsmax": exo.pl_orbsmax,
        }
    }
    return render(request, "catalogue.html",context)


def Sun_planet_orb(name, planet_name, radius_planet, radius_sun, radius_orb=None):
    # In case the orbit data doesn't exist
    if radius_orb is None or math.isnan(radius_orb):
        radius_orb = 1 + (radius_sun * 0.20)

    num_points = 1000

    # Create the orbit path
    theta = np.linspace(0, 2 * np.pi, num_points)
    x_orbit = radius_orb * np.cos(theta)
    y_orbit = radius_orb * np.sin(theta)
    z_orbit = np.zeros_like(x_orbit)

    # Create the planet
    x_planet = [x_orbit[0]]
    y_planet = [y_orbit[0]]
    z_planet = [z_orbit[0]]

    # Create the Earth-like orbit path for reference
    x_orbit_earth = 1 * np.cos(theta)
    y_orbit_earth = 1 * np.sin(theta)
    z_orbit_earth = np.zeros_like(x_orbit_earth)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(0, 0, 0, color="yellow", label="Star", s=radius_sun * 250)

    ax.plot(
        x_orbit,
        y_orbit,
        z_orbit,
        color="white",
        linestyle="dashed",
        label="Exoplanet Orbit",
    )
    ax.plot(
        x_orbit_earth,
        y_orbit_earth,
        z_orbit_earth,
        color="mediumspringgreen",
        linestyle="dashed",
        label="Earth Orbit",
    )

    ax.scatter(
        x_planet,
        y_planet,
        z_planet,
        color="blue",
        label="Exoplanet",
        s=radius_planet * 25,
    )

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_zlim(-1.3, 1.3)
    ax.set_xlabel("X (AU)")
    ax.set_ylabel("Y (AU)")
    ax.set_zlabel("Z (AU)")
    ax.set_title(f"Planet Orbiting Star: {planet_name}", color="white")
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.grid(True)
    ax.tick_params(axis="both", which="major", labelsize=8, colors="white")

    # Set ticks in AU
    ticks = np.linspace(-1.2, 1.2, 7)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_zticks(ticks)

    # Only show every third tick label
    tick_labels = [
        f"{round(tick, 1)} AU" if abs(tick) > 0 else "0 AU" for tick in ticks
    ]
    ax.set_xticklabels(tick_labels)
    ax.set_yticklabels(tick_labels)
    ax.set_zticklabels(tick_labels)

    # Legend
    legend = ax.legend(
        loc="upper right",
        fontsize="small",
        facecolor="dimgray",
        framealpha=1,
        edgecolor="white",
        borderpad=1.25,
        labelspacing=1.5,
        bbox_to_anchor=(1.35, 0.65),
    )
    for text in legend.get_texts():
        text.set_color("white")

    plt.savefig(
        f"{name}.png", dpi=350, bbox_inches="tight", facecolor="black"
    )
    plt.close()

