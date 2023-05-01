#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rle
Version  : 0.9.2
Release  : 19
URL      : https://cran.r-project.org/src/contrib/rle_0.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rle_0.9.2.tar.gz
Summary  : Common Functions for Run-Length Encoded Vectors
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rle-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-rle package.
Group: Libraries

%description lib
lib components for the R-rle package.


%prep
%setup -q -c -n rle
cd %{_builddir}/rle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641097566

%install
export SOURCE_DATE_EPOCH=1641097566
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rle || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rle/COPYRIGHT
/usr/lib64/R/library/rle/DESCRIPTION
/usr/lib64/R/library/rle/INDEX
/usr/lib64/R/library/rle/Meta/Rd.rds
/usr/lib64/R/library/rle/Meta/features.rds
/usr/lib64/R/library/rle/Meta/hsearch.rds
/usr/lib64/R/library/rle/Meta/links.rds
/usr/lib64/R/library/rle/Meta/nsInfo.rds
/usr/lib64/R/library/rle/Meta/package.rds
/usr/lib64/R/library/rle/NAMESPACE
/usr/lib64/R/library/rle/NEWS
/usr/lib64/R/library/rle/NEWS.md
/usr/lib64/R/library/rle/R/rle
/usr/lib64/R/library/rle/R/rle.rdb
/usr/lib64/R/library/rle/R/rle.rdx
/usr/lib64/R/library/rle/help/AnIndex
/usr/lib64/R/library/rle/help/aliases.rds
/usr/lib64/R/library/rle/help/paths.rds
/usr/lib64/R/library/rle/help/rle.rdb
/usr/lib64/R/library/rle/help/rle.rdx
/usr/lib64/R/library/rle/html/00Index.html
/usr/lib64/R/library/rle/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rle/libs/rle.so
/usr/lib64/R/library/rle/libs/rle.so.avx2
/usr/lib64/R/library/rle/libs/rle.so.avx512
