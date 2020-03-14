%MATRIX OPERATIONS IN MATLAB%

transpose(A) %nonconjugate transpose of A%

ctranspose(A) %complex conjugate transpose of A%

mtimes(A,B) %matrix product of A and B%
OR
A*B

mpower(A,B) %A to the power of B%
OR
A^B

sqrtm(A) %principal square root of A%

expm(A) %matrix exponential of A%

logm(A) %principal matrix logarithm of A%

funm(A,function,options,p1,p2,..) %user-defined function at square matrix argument A%

kron(A,B) %Kronecker tensor product of A and B%

cross(A,B,dim) %cross product of A and B along optional dimension dim%

dot(A,B,dim) %dot product of A and B along optional dimension dim%

norm(v) %2-norm a.k.a. Euclidean norm a.k.a. vector magnitude of vector or matrix v%
OR
norm(v,p) %generalized vector p-norm of vector or matrix v%
OR
norm(A,1) %maximum absolute column sum of A%
OR
norm(A,2) %equivalent of norm(X)%
OR
norm(A,Inf) %maximum absolute row sum of A%
OR
norm(A,'fro') %Frobenius norm of A%

normest(A) %estimated 2-norm of A%
OR
normest(A,tol) %estimated 2-norm of A with relative error a.k.a. tolerance tol%

vecnorm(A) %2-norm a.k.a Euclidean norm of A%
OR
vecnorm(A,p,dim) %generalized vector p-norm of A along dimension dim%

cond(A) %2-norm condition number for inversion = ratio of largest singular value of A to the smallest%
OR
cond(A,p) %p-norm condition number for inversion = ratio of largest singular value of A to the smallest%

condest(A) %lower bound value for 1-norm condition number of A%
OR
condest(A,t) %changes t, positive integer equal to # of columns in underlying iteration matrix%

rcond(A) %estimated reciprocal condition of A in 1-norm%

condeig(A) %vector of condition numbers for eigenvalues of A%

det(A) %determinant of square matrix of A%

null(A) %orthonormal basis for nullspace of A%
OR
null(A,'r') %rational basis for nullspace of A, typically not orthonormal%

orth(A) %orthonormal basis for range of A&

rank(A,tol) %rank of A with optional pivot tolerance tol%

rref(A,tol) %reduced row echelon form of A with optional pivot tolerance tol%

trace(A) %sum of diagonal elements of A%

subspace(A,B) %angle between two subspaces specified by columns of A and B%

size()

zeros()

ones()

diag()

horzcat()

eye()

inv()

kron()

vecnorm()

pascal()

magic()

randi()

bandwidth()

tril()

triu()

isbanded()

isdiag()

ishermitian()

issymmetric()

istril()

istriu()

isempty()
