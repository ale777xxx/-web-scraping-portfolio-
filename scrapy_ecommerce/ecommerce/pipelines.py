from itemadapter import ItemAdapter

class CleanProductPipeline:
    def process_item(self, item, spider):
        ad = ItemAdapter(item)
        # normalize fields (example)
        name = (ad.get("name") or "").strip()
        price = (ad.get("price") or "").strip().replace("$","")
        rating = (ad.get("rating") or "").strip()
        ad["name"] = name
        ad["price"] = price
        ad["rating"] = rating
        return item
