# TODO
# - gcc4-c++ collides with gcc-c++:
#   %{_libdir}/libsupc++.a
#   %{_libdir}/libsupc++.la
#
# Conditional build:
%bcond_with	profiling	# build with profiling
%bcond_without	bootstrap	# omit 3-stage bootstrap
%bcond_without	cxx		# build without C++ support
%bcond_with	tests		# torture gcc

%if %{without bootstrap}
%undefine	with_profiling
%endif

%define	sname	gcc
Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl):	Kolekcja kompilatorów GNU: kompilator C i pliki wspó³dzielone
Summary(pt_BR):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
Name:		%{sname}4
Version:	4.1.2
Release:	8
Epoch:		5
License:	GPL v2+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{sname}-%{version}.tar.bz2
# Source0-md5:	a4a3eb15c96030906d8494959eeda23c
Source1:	%{name}-optimize-la.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-nodebug.patch
# -fvisibility fixes...
Patch6:		%{name}-pr19664_gnu_internal.patch
Patch7:		%{name}-pr19664_libstdc++.patch
Patch8:		%{name}-pr20218.patch

# PRs
Patch10:	%{name}-pr7776.patch
Patch11:	%{name}-pr19606.patch
Patch12:	%{name}-pr24879.patch

Patch16:	gcc-4.1-pr29826.patch
Patch17:	%{name}-pr19505.patch
Patch18:	%{name}-pr24419.patch
Patch19:	%{name}-pr24669.patch
Patch20:	%{name}-pr17390.patch
Patch21:	%{name}-pr13676.patch
Patch22:	%{name}-pr25626.patch
Patch23:	%{name}-libstdcxx-bitset.patch

Patch26:	%{name}-ppc64-m32-m64-multilib-only.patch

# 128-bit long double support for glibc 2.4
Patch30:	%{name}-ldbl-default-libstdc++.patch
Patch31:	%{name}-ldbl-default.patch

URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
%{?with_tests:BuildRequires:	autogen}
BuildRequires:	automake
# binutils 2.16.91 or newer are required for compiling medium model now
BuildRequires:	binutils >= 2:2.16.91.0.1
BuildRequires:	bison
BuildRequires:	chrpath >= 0.10
%{?with_tests:BuildRequires:	dejagnu}
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 6:2.3
BuildRequires:	gmp-devel
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.211
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
# AS_NEEDED directive for dynamic linker
# http://sources.redhat.com/ml/glibc-cvs/2005-q1/msg00614.html
# http://sources.redhat.com/ml/binutils/2005-01/msg00288.html
Requires:	binutils >= 2:2.16.90.0.1-0.3
Requires:	libgcc4 = %{epoch}:%{version}-%{release}
Provides:	cpp4 = %{epoch}:%{version}-%{release}
Provides:	gcc = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l es
Un compilador que intenta integrar todas las optimalizaciones y
características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias partes de la colección de compiladores GNU (GCC). Para usar
otro compilador de GCC será necesario que instale el subpaquete
adecuado.

%description -l pl
Kompilator, posiadaj±cy du¿e mo¿liwo¶ci optymalizacyjne niezbêdne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki wspó³dzielone przez ró¿ne
czê¶ci kolekcji kompilatorów GNU (GCC). ¯eby u¿ywaæ innego kompilatora
z GCC, trzeba zainstalowaæ odpowiedni podpakiet.

%description -l pt_BR
Este pacote adiciona infraestrutura básica e suporte a linguagem C ao
GNU Compiler Collection.

%package -n libgcc4
Summary:	Shared gcc library
Summary(es):	Biblioteca compartida de gcc
Summary(pl):	Biblioteka gcc
Summary(pt_BR):	Biblioteca runtime para o GCC
License:	GPL with unlimited link permission
Group:		Libraries
Provides:	libgcc = %{epoch}:%{version}-%{release}

%description -n libgcc4
Shared gcc library.

%description -n libgcc4 -l es
Biblioteca compartida de gcc.

%description -n libgcc4 -l pl
Biblioteka dynamiczna gcc.

%description -n libgcc4 -l pt_BR
Biblioteca runtime para o GCC.

%package c++
Summary:	C++ support for gcc
Summary(es):	Soporte de C++ para gcc
Summary(pl):	Obs³uga C++ dla gcc
Summary(pt_BR):	Suporte C++ para o gcc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-c++ = %{epoch}:%{version}-%{release}
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++

%description c++
This package adds C++ support to the GNU Compiler Collection. It
includes support for most of the current C++ specification, including
templates and exception handling. It does not include a standard C++
library, which is available separately.

%description c++ -l de
Dieses Paket enthält die C++-Unterstützung für den
GNU-Compiler-Collection. Es unterstützt die aktuelle
C++-Spezifikation, inkl. Templates und Ausnahmeverarbeitung. Eine
C++-Standard-Library ist nicht enthalten - sie ist getrennt
erhältlich.

%description c++ -l es
Este paquete añade soporte de C++ al GCC (colección de compiladores
GNU). Ello incluye el soporte para la mayoría de la especificación
actual de C++, incluyendo plantillas y manejo de excepciones. No
incluye la biblioteca estándar de C++, la que es disponible separada.

%description c++ -l fr
Ce package ajoute un support C++ a la collection de compilateurs GNU.
Il comprend un support pour la plupart des spécifications actuelles de
C++, dont les modéles et la gestion des exceptions. Il ne comprend pas
une bibliothéque C++ standard, qui est disponible séparément.

%description c++ -l pl
Ten pakiet dodaje obs³ugê C++ do kompilatora gcc. Ma wsparcie dla
du¿ej ilo¶ci obecnych specyfikacji C++, nie zawiera natomiast
standardowych bibliotek C++, które s± w oddzielnym pakiecie.

%description c++ -l pt_BR
Este pacote adiciona suporte C++ para o gcc.

%description c++ -l tr
Bu paket, GNU C derleyicisine C++ desteði ekler. 'Template'ler ve
aykýrý durum iþleme gibi çoðu güncel C++ tanýmlarýna uyar. Standart
C++ kitaplýðý bu pakette yer almaz.

%package -n libstdc++4
Summary:	GNU C++ library
Summary(es):	Biblioteca C++ de GNU
Summary(pl):	Biblioteki GNU C++
Summary(pt_BR):	Biblioteca C++ GNU
License:	GPL v2+ with free software exception
Group:		Libraries
Provides:	libstdc++ = %{epoch}:%{version}-%{release}
Obsoletes:	libg++
Obsoletes:	libstdc++3

%description -n libstdc++4
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++4 -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++4 -l es
Este es el soporte de las bibliotecas padrón del C++, junto con
herramientas GNU adicionales. El paquete incluye las bibliotecas
compartidas necesarias para ejecutar aplicaciones C++.

%description -n libstdc++4 -l fr
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++4 -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim biblioteki dynamiczne niezbêdne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++4 -l pt_BR
Este pacote é uma implementação da biblioteca padrão C++ v3, um
subconjunto do padrão ISO 14882.

%description -n libstdc++4 -l tr
Bu paket, standart C++ kitaplýklarýnýn GNU gerçeklemesidir ve C++
uygulamalarýnýn koþturulmasý için gerekli kitaplýklarý içerir.

%package -n libstdc++4-devel
Summary:	Header files and documentation for C++ development
Summary(de):	Header-Dateien zur Entwicklung mit C++
Summary(es):	Ficheros de cabecera y documentación para desarrollo C++
Summary(fr):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki standardowej C++
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o desenvolvimento em C++
Summary(tr):	C++ ile program geliþtirmek için gerekli dosyalar
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	glibc-devel
Requires:	libstdc++4 = %{epoch}:%{version}-%{release}
Provides:	libstdc++-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libg++-devel
Obsoletes:	libstdc++3-devel

%description -n libstdc++4-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files needed for C++ development and
library documentation.

%description -n libstdc++4-devel -l es
Este es el soporte de las bibliotecas padrón del lenguaje C++. Este
paquete incluye los archivos de inclusión y bibliotecas necesarios
para desarrollo de programas en lenguaje C++.

%description -n libstdc++4-devel -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++. Znajduj± siê w nim pliki nag³ówkowe wykorzystywane przy
programowaniu w jêzyku C++ oraz dokumentacja biblioteki standardowej.

%description -n libstdc++4-devel -l pt_BR
Este pacote inclui os arquivos de inclusão e bibliotecas necessárias
para desenvolvimento de programas C++.

%package -n libstdc++4-static
Summary:	Static C++ standard library
Summary(es):	Biblioteca estándar estática de C++
Summary(pl):	Statyczna biblioteka standardowa C++
License:	GPL v2+ with free software exception
Group:		Development/Libraries
Requires:	libstdc++4-devel = %{epoch}:%{version}-%{release}
Provides:	libstdc++-static = %{epoch}:%{version}-%{release}

%description -n libstdc++4-static
Static C++ standard library.

%description -n libstdc++4-static -l es
Biblioteca estándar estática de C++.

%description -n libstdc++4-static -l pl
Statyczna biblioteka standardowa C++.

%prep
%setup -q -n gcc-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# -fvisbility fixes...
%patch6 -p1
%patch7 -p1
%patch8 -p1

# PRs
%patch10 -p1
%patch11 -p0
%patch12 -p0

cd gcc
%patch16 -p0
cd -
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%patch26 -p1

%patch30 -p0
%patch31 -p0

# because we distribute modified version of gcc...
sed -i 's:#define VERSUFFIX.*:#define VERSUFFIX " (PLD-Linux)":' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

mv ChangeLog ChangeLog.general

%build
cd gcc
%{__autoconf}
cd ..
cp -f /usr/share/automake/config.sub .

rm -rf builddir && install -d builddir && cd builddir

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--program-suffix="4" \
	--prefix=%{_prefix} \
	--with-local-prefix=%{_prefix}/local \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--x-libraries=%{?_x_libraries}%{!?_x_libraries:%{_libdir}} \
	--enable-shared \
	--enable-threads=posix \
	--enable-languages="c%{?with_cxx:,c++}" \
	--enable-c99 \
	--enable-long-long \
	--enable-nls \
	--disable-werror \
	--with-gnu-as \
	--with-gnu-ld \
	--with-demangler-in-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
%ifnarch ia64
	--without-system-libunwind \
%else
	--with-system-libunwind \
%endif
	--without-x \
	--disable-multilib \
%if %{with cxx}
	--with-gxx-include-dir=%{_includedir}/c++/%{version} \
	--disable-libstdcxx-pch \
	--enable-__cxa_atexit \
	--enable-libstdcxx-allocator=new \
%endif
	%{_target_platform}

cd ..

%{__make} -C builddir \
	%{?with_bootstrap:%{?with_profiling:profiled}bootstrap} \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags} -O0" \
	GNATLIBCFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%{?with_tests:%{__make} -k -C builddir check 2>&1 ||:}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd builddir

%{__make} -j1 install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

install gcc/specs $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}/%{version}

%ifarch sparc64
ln -sf	%{_bindir}/sparc64-pld-linux-gcc4 \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc4
%endif

ln -sf %{_bindir}/cpp4 $RPM_BUILD_ROOT/lib/cpp4
ln -sf gcc4 $RPM_BUILD_ROOT%{_bindir}/cc4
echo ".so gcc4.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc4.1

mv $RPM_BUILD_ROOT{%{_libdir}/libssp.so.*,%{_slibdir}}
ln -sf %{_slibdir}/$(basename $RPM_BUILD_ROOT%{_slibdir}/libssp.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libssp.so
chmod +x $RPM_BUILD_ROOT%{_slibdir}/libgcc_s.so.1
# rename so we could be installed with system gcc.spec
mv $RPM_BUILD_ROOT%{_slibdir}/libgcc_s.so.{1,%{version}}
ln -s libgcc_s.so.%{version} $RPM_BUILD_ROOT%{_slibdir}/libgcc_s.so.1

cd ..

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/)
mkdir	$gccdir/tmp

# we have to save these however
mv $gccdir/include/syslimits.h $gccdir/tmp
mv $gccdir/include/ssp $gccdir/tmp
rm -rf $gccdir/include
mv $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools

%find_lang gcc
%find_lang cpplib
cat cpplib.lang >> gcc.lang

%if %{with cxx}
%find_lang libstdc\+\+
install libstdc++-v3/include/stdc++.h $RPM_BUILD_ROOT%{_includedir}
%endif

# cvs snap doesn't contain (release does) below files,
# so let's create dummy entries to satisfy %%files.
[ ! -f NEWS ] && touch NEWS

# not packaged anywhere
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_infodir}/cpp.info
rm -f $RPM_BUILD_ROOT%{_infodir}/cppinternals.info
rm -f $RPM_BUILD_ROOT%{_infodir}/gcc.info
rm -f $RPM_BUILD_ROOT%{_infodir}/gccinstall.info
rm -f $RPM_BUILD_ROOT%{_infodir}/gccint.info
rm -f $RPM_BUILD_ROOT%{_includedir}/mf-runtime.h
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/fsf-funding.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gfdl.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gpl.7
# don't build these then?
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflap.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflap.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflap.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflap.so.0
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflap.so.0.0.0
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflapth.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflapth.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflapth.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflapth.so.0
rm -f $RPM_BUILD_ROOT%{_libdir}/libmudflapth.so.0.0.0

# remove empty language catalogs (= 1 message only)
find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	-p /sbin/ldconfig -n libgcc4
%postun	-p /sbin/ldconfig -n libgcc4

%post	-p /sbin/ldconfig -n libstdc++4
%postun	-p /sbin/ldconfig -n libstdc++4

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS NEWS
# bugs.html faq.html
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%dir %{_libdir}/gcc/*/*/include
%dir %{_libdir}/gcc/*/*/include/ssp

%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/gcc4
%attr(755,root,root) %{_bindir}/gccbug4
%attr(755,root,root) %{_bindir}/gcov4
%attr(755,root,root) %{_bindir}/cc4
%attr(755,root,root) %{_bindir}/cpp4

%{_mandir}/man1/cc4.1*
%{_mandir}/man1/cpp4.1*
%{_mandir}/man1/gcc4.1*
%{_mandir}/man1/gcov4.1*

%attr(755,root,root) /lib/cpp4
%attr(755,root,root) %{_slibdir}/libgcc_s.so
%{_libdir}/libssp.a
%{_libdir}/libssp.la
%attr(755,root,root) %{_libdir}/libssp.so
%{_libdir}/libssp_nonshared.a
%{_libdir}/libssp_nonshared.la
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%{_libdir}/gcc/*/*/crt*.o
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2

%{_libdir}/gcc/*/*/include/*.h
%{_libdir}/gcc/*/*/include/ssp/*.h

%files -n libgcc4
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/libssp.so.*.*.*
%attr(755,root,root) %ghost %{_slibdir}/libssp.so.0
%attr(755,root,root) %{_slibdir}/libgcc_s.so.%{version}

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%doc gcc/cp/{ChangeLog,NEWS}
%attr(755,root,root) %{_bindir}/g++4
%attr(755,root,root) %{_bindir}/*-g++4
%attr(755,root,root) %{_bindir}/c++4
%attr(755,root,root) %{_bindir}/*-c++4
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1plus
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%{_mandir}/man1/g++4.1*

%files -n libstdc++4 -f libstdc++.lang
%defattr(644,root,root,755)
%doc libstdc++-v3/{ChangeLog,README}
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstdc++.so.6

%files -n libstdc++4-devel
%defattr(644,root,root,755)
%doc libstdc++-v3/docs/html
%dir %{_includedir}/c++
%{_includedir}/stdc++.h
%{_includedir}/c++/%{version}
%{_libdir}/libstdc++.la
%attr(755,root,root) %{_libdir}/libstdc++.so

%files -n libstdc++4-static
%defattr(644,root,root,755)
%{_libdir}/libstdc++.a
%endif
