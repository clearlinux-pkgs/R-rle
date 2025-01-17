#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-rle
Version  : 0.9.2
Release  : 24
URL      : https://cran.r-project.org/src/contrib/rle_0.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rle_0.9.2.tar.gz
Summary  : Common Functions for Run-Length Encoded Vectors
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rle-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-rle package.
Group: Libraries

%description lib
lib components for the R-rle package.


%prep
%setup -q -n rle
pushd ..
cp -a rle buildavx2
popd
pushd ..
cp -a rle buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737156368

%install
export SOURCE_DATE_EPOCH=1737156368
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/R/library/rle/libs/rle.so
/V4/usr/lib64/R/library/rle/libs/rle.so
/usr/lib64/R/library/rle/libs/rle.so
