plot(t, rad2deg(y[:, 3:]))
xlabel('Time [s]')
ylabel('Angle [deg]')
legend(["${}$".format(vlatex(s)) for s in speeds])