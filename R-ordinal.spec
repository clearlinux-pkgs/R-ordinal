#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ordinal
Version  : 2019.3.9
Release  : 7
URL      : https://cran.r-project.org/src/contrib/ordinal_2019.3-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ordinal_2019.3-9.tar.gz
Summary  : Regression Models for Ordinal Data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-ordinal-lib = %{version}-%{release}
Requires: R-lme4
Requires: R-numDeriv
Requires: R-ucminf
Requires: R-xtable
BuildRequires : R-lme4
BuildRequires : R-numDeriv
BuildRequires : R-ucminf
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
as ordered regression models, proportional odds models, proportional
    hazards models for grouped survival times and ordered logit/probit/...
    models. Estimation is via maximum likelihood and mixed models are fitted
    with the Laplace approximation and adaptive Gauss-Hermite quadrature.
    Multiple random effect terms are allowed and they may be nested, crossed or
    partially nested/crossed. Restrictions of symmetry and equidistance can be
    imposed on the thresholds (cut-points/intercepts). Standard model
    methods are available (summary, anova, drop-methods, step,
    confint, predict etc.) in addition to profile methods and slice
    methods for visualizing the likelihood function and checking
    convergence.

%package lib
Summary: lib components for the R-ordinal package.
Group: Libraries

%description lib
lib components for the R-ordinal package.


%prep
%setup -q -c -n ordinal

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552184192

%install
export SOURCE_DATE_EPOCH=1552184192
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinal
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ordinal
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ordinal|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ordinal/CITATION
/usr/lib64/R/library/ordinal/DESCRIPTION
/usr/lib64/R/library/ordinal/INDEX
/usr/lib64/R/library/ordinal/Meta/Rd.rds
/usr/lib64/R/library/ordinal/Meta/data.rds
/usr/lib64/R/library/ordinal/Meta/features.rds
/usr/lib64/R/library/ordinal/Meta/hsearch.rds
/usr/lib64/R/library/ordinal/Meta/links.rds
/usr/lib64/R/library/ordinal/Meta/nsInfo.rds
/usr/lib64/R/library/ordinal/Meta/package.rds
/usr/lib64/R/library/ordinal/Meta/vignette.rds
/usr/lib64/R/library/ordinal/NAMESPACE
/usr/lib64/R/library/ordinal/NEWS
/usr/lib64/R/library/ordinal/R/ordinal
/usr/lib64/R/library/ordinal/R/ordinal.rdb
/usr/lib64/R/library/ordinal/R/ordinal.rdx
/usr/lib64/R/library/ordinal/data/Rdata.rdb
/usr/lib64/R/library/ordinal/data/Rdata.rds
/usr/lib64/R/library/ordinal/data/Rdata.rdx
/usr/lib64/R/library/ordinal/doc/clm_article.R
/usr/lib64/R/library/ordinal/doc/clm_article.Rnw
/usr/lib64/R/library/ordinal/doc/clm_article.pdf
/usr/lib64/R/library/ordinal/doc/clmm2_tutorial.R
/usr/lib64/R/library/ordinal/doc/clmm2_tutorial.Rnw
/usr/lib64/R/library/ordinal/doc/clmm2_tutorial.pdf
/usr/lib64/R/library/ordinal/doc/index.html
/usr/lib64/R/library/ordinal/help/AnIndex
/usr/lib64/R/library/ordinal/help/aliases.rds
/usr/lib64/R/library/ordinal/help/ordinal.rdb
/usr/lib64/R/library/ordinal/help/ordinal.rdx
/usr/lib64/R/library/ordinal/help/paths.rds
/usr/lib64/R/library/ordinal/html/00Index.html
/usr/lib64/R/library/ordinal/html/R.css
/usr/lib64/R/library/ordinal/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ordinal/libs/ordinal.so
/usr/lib64/R/library/ordinal/libs/ordinal.so.avx2
/usr/lib64/R/library/ordinal/libs/ordinal.so.avx512
