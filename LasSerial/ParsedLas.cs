using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LasSerial
{
    internal class ParsedLas
    {
        public List<LasInfo> Version = new List<LasInfo>();

        public List<LasInfo> Well = new List<LasInfo>();

        public List<LasInfo> Parameters = new List<LasInfo>();

        public List<LasInfo> Curves = new List<LasInfo>();

        public List<List<double?>> data = new List<List<double?>>(); 
    }
}
