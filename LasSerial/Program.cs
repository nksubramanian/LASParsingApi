// See https://aka.ms/new-console-template for more information
using LasSerial;
using Newtonsoft.Json;
using RestSharp;
using System.Net.Http.Headers;

Console.WriteLine("Hello, World!");
LasInfo lasinfo1 = new LasInfo{mnemonic = "subbu", unit = "ft", value = "fggf", descr = "dfsd"};
LasInfo lasinfo2 = new LasInfo { mnemonic = "sufddfbbu", unit = "ft", value = "fggf", descr = "dfsd" };

var x = new ParsedLas();
x.Version.Add(lasinfo1);
x.Version.Add(lasinfo2);




double[] items1 = { 1, 2, 3, 4, 5, 6, 7 };
List<double> elementlist1 = new List<double>(items1);

double[] items2 = { 1, 2, 3, 4, 5, 6, 7 };
List<double> elementlist2 = new List<double>(items2);


using (var httpClient = new HttpClient())
{
    using (var request = new HttpRequestMessage(new HttpMethod("GET"), "http://127.0.0.1:5000/getparsedinfo"))
    {
        var multipartContent = new MultipartFormDataContent();
        multipartContent.Add(new ByteArrayContent(File.ReadAllBytes(@"D:\LasSerial\LAS_2.las")), "file", Path.GetFileName(@"D:\LasSerial\LAS_2.las"));
        request.Content = multipartContent;

        var response = await httpClient.SendAsync(request);
        var g = response.Content.ReadAsStringAsync().Result;
        var result = JsonConvert.DeserializeObject<ParsedLas>(g);
        Console.WriteLine(g);
    }
}