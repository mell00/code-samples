%MATLAB PLOTTING%

%General 2D and 3D graphics:%
title('name_of_plot')

xlabel('name_of_x_axis')

ylabel('name_of_y_axis')

legend('name_of_1st_curve','name_of_2nd_curve')


%2D line plots:%
plot(y)

plot(x,y)

plot(x,A)

stairs()

errorbar()

area()

stackedplot()

fplot(@(x) some_expression, [a,b])

fimplicit()

loglog(x,y)

semilogx(x,y)

semilogy(x,y)

%3D line plots:%
plot3(y)

plot3(x,y)

plot3(x,A)

fplot3(@(x) some_expression, [a,b])

subplot()

axis equal

grid

hold on

figure

%2D data distribution plots:%
histogram(A,nbins,'BinEdges',edges,'BinCounts',counts)
OR
histogram(A,name_of_param,value_of_param)

h = histogram(_)


%3D data distribution plots:%
histogram2(X,Y,nbins,)

%2D discrete data plots:%


%3D discrete data plots:%


%2D geographic plots:%


%3D geographic plots:%


%polar plots:%


%2D contour plots:%


%3D contour plots:%


%vector fields:%


%2D polygons:%


%3D surfaces, volumes, and polygons:%


%2D animation:%


%3D animation:%
