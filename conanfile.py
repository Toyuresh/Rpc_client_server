from conans import ConanFile, CMake


class CppdummyConan(ConanFile):
    name = "cppdummy"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Cppdummy here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"
    requires = (("boost/1.70.0@conan/stable"),
                ("OpenSSL/1.0.2s@conan/stable"),
                ("jsonformoderncpp/3.6.1@vthiery/stable"),
                ("libpq/9.6.9@bincrafters/stable"),
                ("libpqxx/6.4.5@bincrafters/stable"),
                ("protobuf/3.6.1@bincrafters/stable"),
                ("protoc_installer/3.6.1@bincrafters/stable"),
                )

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.hpp", dst="include", src="src")
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.cc", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.cfg", dst="bin", keep_path=False)
        self.copy("*test", dst="bin", keep_path=False)
        self.copy("*client", dst="bin", keep_path=False)
        self.copy("*server", dst="bin",keep_path=False)
        self.copy("*postgres_test", dst="bin",keep_path=False)

   # def package_info(self):
    #    self.cpp_info.libs = ["hello"]
