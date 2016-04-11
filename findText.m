% First test
%
% Make sure you have the image package (if using Octave). Once in your local
% installation you load it with:
%
% >> pkg load image
%
% History:
%     18.08.2015. First implementation.
%
% @author: Mario Garcia
% www.mayitzin.com

clear all
 
disp('Starting test')
 
I = imread('page001.png');
I = rgb2gray(I);
[m, n] = size(I);

% Sharpening Filters
f1 = fspecial('unsharp', 0.1);
f2 = fspecial('unsharp', 0.9);

% Sharped Images
J1 = imfilter(I,f1);
J2 = imfilter(I,f2);

% Binarized Images
t = 220;
Ibw1 = im2bw(J1,t/256);
Ibw2 = im2bw(J2,t/256);

% Dilate image
se2 = strel('square',5);
Idi2 = ~imdilate(~Ibw2,se2);

% Close Image
se3 = strel('square',5);
Idi3= ~imclose(~Ibw2,se3);
%Idi3 = ~bwconvhull(~Idi3, 'objects');

% Centroids
Ics2 = regionprops(~Idi2,'centroid');
cs2 = cat(1, Ics2.Centroid);

% Pseudo-Histograms
x = sum(~Ibw2,2);
y = zeros(m,1);
for i = 1:m
    y(i) = sum(round(cs2(:,2))==i);
end
z = x.*y;
wx = sum(~Idi3,1);
wy = sum(~Idi3,2);

y1 = 0;
y2 = 0;
x1 = 0;
x2 = 0;
stops = zeros(m,1);

for i=1:m
    if (wy(i)>10)
        stops(i) = 1;
    end
    if (wy(i)>10 && y1==0)
        y1 = i;
    elseif (wy(i)>10 && y1>0)
        y2 = i;
    end
end

for i=1:n
    if (wx(i)>20 && x1==0) 
    x1 = i;
    elseif (wx(i)>20 && x1>0)
    x2 = i;
    end
end

% Plotting Images
figure()
% subplot(1,4,1)
%     imshow(I);
subplot(1,3,1)
    imshow(I); hold on
    plot(cs2(:,1),cs2(:,2), 'r*'); hold off
%subplot(1,4,2) % Histogram of Pixels
%    plot(gca, 1:m,x, 'r-')
%    set(gca,'view',[90 90])
%subplot(1,4,3)
%    plot(gca, 1:n,wx, 'r-')
%    set(gca,'view',[90 90])
%subplot(1,4,4)
%    plot(gca, 1:m,wy, 'r-')
%    set(gca,'view',[90 90])
subplot(1,3,2)
    imshow(Idi3)
    hold on
    plot([x1, x2, x2, x1, x1],[y1, y1, y2, y2, y1],'r-')
    hold off
subplot(1,3,3)
    plot(gca, 1:m,stops, 'r-')
    set(gca,'view',[90 90])
