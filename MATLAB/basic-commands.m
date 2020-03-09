%MATLAB BASIC COMMANDS%

save 'file.mat'

load 'file.mat'

diary on

diary off

whos

clear

help command

doc command

x = 1

x = [1 2 3]

x = [1 2 3];

x = [1; 2; 3]

A = [1 2 3 4; 5 6 7 8; 9 10 11 12];
x(2) = 7
A(2,1) = 0

x * 1

x + 1

x + y

A * y

A * B

x .* y

A^2

x^2

x.^2

cos(x)

abs(A)

exp(A)

sqrt(A)

expm(A)

sqrtm(A)

x.', A.'

x', A'

x' * y

dot(x,y)

sum(x.*y)

x * y'

rand(3,4)

randn(3,4)

zeros(3,4)

ones(3,4)

eye(4)

eye(3,4)

linspace(2.5,3.5,100)

3:4

diag(x)

diag(A)

x(3:6)

x(3:end)

x(1:3:end)

x(:)

A(2,:)

A(2,1:3)

A(:,2)

A \ b

inv(A)

[C,B,P] = lu(A)

eig(A)

[E,F] = eig(A)

plot(y)

plot(x,y)

plot(x,A)

loglog(x,y)

semilogx(x,y)

semilogy(x,y)

fplot(@(x) some_expression, [a,b])

axis equal

title('name_of_plot')

xlabel('name_of_x_axis')

ylabel('name_of_y_axis')

legend('name_of_1st_curve','name_of_2nd_curve')

grid

figure
